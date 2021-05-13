n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())

a = {}
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        v = x[j] - x[i], y[j] - y[i]
        if v not in a:
            a[v] = 1
        else:
            a[v] += 1
ans = n
# print("a =", a)
if len(a.values()) > 0:
    ans -= max(a.values())
print(ans)