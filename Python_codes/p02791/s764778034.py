
N = int(input())
X = list(map(int, input().split()))

ans = 0
cur = 10 ** 6
for i in range(N):
    if X[i] <= cur:
        ans += 1
    cur = min(cur, X[i])

print(ans)
