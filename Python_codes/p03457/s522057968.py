n = int(input())

tn = 0
xn = 0
yn = 0
j = True
for i in range(n):
    td, xd, yd = map(int, input().split())
    t = td - tn
    x = abs(xd - xn)
    y = abs(yd - yn)
    xn = xd
    yn = yd
    tn = td
    if t%2 == (x + y)%2 and (x + y) <= t:
        continue
    j = False
if j:
    print("Yes")
else:
    print("No")
