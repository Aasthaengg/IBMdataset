n, m = map(int, input().split())

xsum = 0
xx = [int(i) for i in input().split()]
for i, x in enumerate(xx):
    xsum += (2 * i - n + 1) * x

ysum = 0
yy = [int(i) for i in input().split()]
for i, y in enumerate(yy):
    ysum += (2 * i - m + 1) * y

print(xsum * ysum % 1000000007)