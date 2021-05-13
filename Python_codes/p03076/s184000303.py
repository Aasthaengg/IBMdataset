a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = 10
ans = 0
for i in (a, b, c, d, e):
    q, mod = divmod(i, 10)
    if mod == 0:
        ans += i
    else:
        m = min(m, mod)
        ans += (q + 1) * 10
print(ans - 10 + m)
