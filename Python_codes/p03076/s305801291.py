from math import ceil

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

x = min((a - 1) % 10, (b - 1) % 10, (c - 1) % 10, (d - 1) % 10, (e - 1) % 10) + 1
ans = ceil(a / 10) * 10 + ceil(b / 10) * 10 + ceil(c / 10) * 10 + ceil(d / 10) * 10 + ceil(e / 10) * 10
ans -= (10 - x)
print(ans)
