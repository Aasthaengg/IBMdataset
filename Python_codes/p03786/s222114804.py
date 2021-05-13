# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    A.sort()
    s = 0
    dp = [0] * (N + 1)
    for i, a in enumerate(A):
        dp[i + 1] = 1
        if a <= s * 2: dp[i + 1] += dp[i]
        s += a
    print(dp[N])

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
