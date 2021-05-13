#coding:utf-8
n, m, d = map(int,input().split())
if d == 0:
    sums = n
else:
    sums = 2*n - 2*d
a = (m-1) * (sums / n ** 2 )
print(a)
