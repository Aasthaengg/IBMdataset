import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

p_array = list(map(float, stdin.readline().split()))

dp = [0] * (N+1)
dp[0] = 1

for p in p_array:
    for i in range(N, 0, -1):
        dp[i] = dp[i] * (1-p) + dp[i-1] * p
    dp[0] *= (1-p)


print(sum(dp[(N+1)//2:]))
