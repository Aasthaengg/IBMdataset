N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
ans = 0
if D <= X:
    ans += 1
for l in L:
    D = l + D
    if D <= X:
        ans += 1

print(ans)
