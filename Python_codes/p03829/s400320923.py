n, a, b = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(1,n):
    walk = (X[i] - X[i-1]) * a
    tel = b
    if walk >= tel:
        ans += tel
    else:
        ans += walk
print(ans)