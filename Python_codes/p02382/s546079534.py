import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

Dp1 = 0
Dp2 = 0
Dp3 = 0
Dp4 = []
for i in range(n):
 xyi = abs(x[i] - y[i])
 Dp1 += xyi
 Dp2 += xyi ** 2
 Dp3 += xyi ** 3
 Dp4.append(xyi)
print("{0:05f}".format(Dp1))
print("{0:05f}".format(math.sqrt(Dp2)))
print("{0:05f}".format(math.pow(Dp3, (1 / 3))))
print("{0:05f}".format(max(Dp4)))