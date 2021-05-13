import sys

sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline

######################################################

INF = 1e10

N, K = [int(_) for _ in input().split()]


def f(b):
    """
    a= b*x + r
    a=[0,N] まで回すとき, あまり r は 0,1,...,b-1 と順番に出現する. (x = a//b)
    """
    p = (N // b)  # r が p 回 [0,b-1] をループ
    ans = max(p * (b - K), 0)

    # 残りの分
    ans += max(N % b - K + 1, 0)

    if K == 0:
        ans -= 1

    return ans

def main():
    ans =0
    for b in range(1,N+1):
        ans+=f(b)
    print(ans)
main()

