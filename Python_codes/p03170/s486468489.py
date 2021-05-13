N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_a = A[-1]

dp = [0] * (K+1)

for a in A:
    dp[a] = 1

for i in range(1, K + 1):
    bl = False
    for a in A:
        if i - a < 0:
            break
        if dp[i - a] == 0:
            bl = True
            break
    dp[i] = 1 if bl else 0


ans = "First" if dp[K] else "Second"
print(ans)
