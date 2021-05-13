
N = int(input())
X = list(map(int, input().split()))

ans = 0
cnt = 0
cur = X[0]
for i in range(1, N):
    if cur < X[i]:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1
    cur = X[i]

print(max(ans, cnt))
