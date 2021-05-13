n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
a = a[::-1]
b = b[::-1]

ans = 0
for i in range(n):
    t = (a[i] + ans) % b[i]
    if t != 0:
        ans += b[i]-t

print(ans)