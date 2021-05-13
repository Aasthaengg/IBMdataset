import math
n, m, d = map(int, input().split())
num = 0

if d > n - 1:
    num = 0
elif d == 0:
    num = (n - d)
else:
    num = (n - d) * 2


ans = num*  (m-1)/(n*n)
print(ans)


# elif d == n - 1:
#     num = m - 1
# elif 2 * d > n - 1:
#     num = (n - d) * (m - 1)


# n, m, s, t = map(int, input().split())
# u = []
# v = []
# a = []
# b = []
#
# for i in range(m):
#     in1, in2, in3, in4 = map(int, input().split())
#
#     u.append(in1)
#     v.append(in2)
#     a.append(in3)
#     b.append(in4)
#
# print(u,v,a,b)


