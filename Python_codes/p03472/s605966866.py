import math

n, h = map(int, input().split())
b = [0] * n
maxa = 0
for i in range(n):
    x, y = map(int, input().split())
    maxa = max(x, maxa)
    b[i] = y
b.sort(reverse = True)
ans = 0
for i in range(n):
    if b[i] < maxa:
        break
    h -= b[i]
    ans += 1
    if h <= 0:
        break
if not h <= 0:
    ans += math.ceil(h / maxa)
print(ans)