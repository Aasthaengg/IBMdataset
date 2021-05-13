X, N = map(int, input().split())
P = set(map(int, input().split()))

sub = 10000
ans = 0
for i in range(-1000, 1001):
    y = X + i
    if y in P:
        continue
    if abs(i) < sub:
        sub = abs(i)
        ans = y
print(ans)