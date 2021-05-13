import sys
sys.setrecursionlimit(10**6)

N = int(input())
a, b, c = [], [], []
dp = [[0] * 3 for _ in range(N+1)]

for i in range(N):
    v1, v2, v3 = map(int, input().split())
    a.append(v1)
    b.append(v2)
    c.append(v3)

def solve(idx, prev):
    if dp[idx][prev] > 0:
        return dp[idx][prev]

    if idx == N:
        dp[idx][prev] = 0
    elif idx == 0:
        v1 = solve(idx + 1, 0) + a[idx]
        v2 = solve(idx + 1, 1) + b[idx]
        v3 = solve(idx + 1, 2) + c[idx]
        dp[idx][prev] = max(v1, v2, v3)

    # Prev was A
    elif prev == 0:
        # Select B
        a1 = solve(idx + 1, 1) + b[idx]
        # Select C
        a2 = solve(idx + 1, 2) + c[idx]
        dp[idx][prev] = max(a1, a2)

    # Prev was B
    elif prev == 1:
        # Select A
        b1 = solve(idx + 1, 0) + a[idx]
        # Select C
        b2 = solve(idx + 1, 2) + c[idx]
        dp[idx][prev] = max(b1, b2)

    # Prev was B
    elif prev == 2:
        # Select A
        c1 = solve(idx + 1, 0) + a[idx]
        # Select B
        c2 = solve(idx + 1, 1) + b[idx]
        dp[idx][prev] = max(c1, c2)

    return dp[idx][prev]

print(solve(0, 0))