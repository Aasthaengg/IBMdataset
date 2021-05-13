import sys
from math import gcd
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)

def main():
    N, Ma, Mb = map(int, input().split())
    """
    dp[i][j] = (0~iまでの薬品を使って、物質Bがjグラム余るようにするときの最小金額)
    jは整数になるとは限らないのでj=p/qと既約分数表示して(p, q)を辞書のキーとして保持する。
    """
    dp = {}
    a, b, c = map(int, input().split())
    p, q = b * Ma - a * Mb, Ma
    div = gcd(p, q)
    p, q = p // div, q // div
    dp[(p, q)] = c
    #print("i=0=>dp={}".format(dp))

    for i in range(1, N):
        dp2 = {}
        a, b, c = map(int, input().split())
        p, q = b * Ma - a * Mb, Ma
        div = gcd(p, q)
        p, q = p // div, q // div
        dp2[(p, q)] = c
        for p, q in dp:
            cost = dp[(p, q)]
            if (p, q) in dp2:
                dp2[(p, q)] = min(dp2[(p, q)], cost)
            else:
                dp2[(p, q)] = cost
            np, nq = p * Ma + b * q * Ma - a * q * Mb, q * Ma
            if np == 0:
                np, nq = 0, 1
            else:
                div = gcd(np, nq)
                np, nq = np // div, nq // div
            if (np, nq) in dp2:
                dp2[(np, nq)] = min(dp2[(np, nq)], cost + c)
            else:
                dp2[(np, nq)] = cost + c
        dp = dp2
        #print("i={}=>dp={}".format(i, dp))
    if (0, 1) in dp:
        print(dp[(0, 1)])
    else:
        print(-1)



if __name__ == "__main__":
    main()
