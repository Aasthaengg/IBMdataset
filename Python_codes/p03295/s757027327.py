n, m = map(int, input().split())
X = []
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    X.append((b,a))
X.sort()

pre_b = -1
ans = 0
for i in range(m):
    b, a = X[i]
    if a >= pre_b:
        ans += 1
        pre_b = b
print(ans)
