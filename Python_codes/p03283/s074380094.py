
import sys
sys.setrecursionlimit(10**6)
dp = []
train = []

def subq(l, r):
    global dp, train
    if l == 0 or r == 0:
        return 0
    else:
        tmp1 = dp[l][r]
        if tmp1 != -1:
            return tmp1
        else:
            tmp2 = train[l][r] + subq(l - 1, r) + subq(l, r - 1) -  subq(l - 1, r - 1)
            dp[l][r] = tmp2
            return tmp2

def main():
    global dp, train
    n, m, qn = map(int, input().split())
    dp = [[-1] * (n+1) for _ in range(n+1)]
    train = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        l, r = map(int, input().split())
        train[int(l)][int(r)] += 1

    for _ in range(qn):
        p, q = map(int, input().split())
        r = subq(q, q) - subq(p-1, q) - subq(q, p-1) + subq(p-1, p-1)
        print(r)

if __name__ == '__main__':
    main()
