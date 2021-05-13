r, D, x2000 = map(int, input().split())

x2001 = r*x2000-D

print(x2001)

xx = x2001

for i in range(1, 10):
    xx = xx*r-D
    print(xx)
