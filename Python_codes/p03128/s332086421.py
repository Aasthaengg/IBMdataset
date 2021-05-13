N, M = map(int, input().split())
A = list(map(int, input().split()))

match = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

dp = ["-" for _ in range(11000)]
dp[0] = ""


def _max(a, b):
    if len(a) > len(b):
        return a
    if len(a) < len(b):
        return b
    return max(a, b)


for i in range(N+1):
    if dp[i] == "-":
        continue
    for a in A:
        dp[i+match[a]] = _max(dp[i+match[a]], dp[i]+str(a))

print(dp[N])

