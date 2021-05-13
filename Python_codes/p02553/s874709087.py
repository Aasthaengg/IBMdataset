a, b, c, d = map(int, input().split())
xy1 = xy2 = xy = 0

k = a*c
l = a*d
m = b*c
n = b*d

if k >= l:
    xy1 = k
else:
    xy1 = l

if m >= n:
    xy2 = m
else:
    xy2 = n

if xy1 >= xy2:
    xy = xy1
else:
    xy = xy2

print(xy)