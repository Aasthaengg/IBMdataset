n, m = map(int, input().split())
X = []
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    X.append((b, a))

X.sort()
c = -1
ans = 0
for i in range(m):
    b, a = X[i]
    if a < c:
        continue
    else:
        ans += 1
    c = b
print(ans)
