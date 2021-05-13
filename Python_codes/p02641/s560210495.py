X, N = map(int, input().split())
P = list(map(int, input().split()))

best = float('inf')
ans = -1
for a in range(102):
    if a in P:
        continue
    if best > abs(X - a):
        best = abs(X - a)
        ans = a
print(ans)
