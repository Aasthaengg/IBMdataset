N, M, X = map(int, input().split())
A = list(map(int, input().split()))

ans1 = 0
for i in range(0, X + 1):
    if i in A:
        ans1 += 1

ans2 = 0
for i in range(X, N):
    if i in A:
        ans2 += 1

ans = min(ans1, ans2)
print(ans)
