n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = [0]
y = [0]
for i in range(n):
    x.append(a[i] + x[i])
for j in range(m):
    y.append(b[j] + y[j])
ans = 0
q = m
for p in range(n + 1):
    if x[p] > k:
        break
    while y[q] > k - x[p]:
        q = q - 1
    ans = max(ans, p + q)
print(ans)