from bisect import *
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
c.sort()
res = 0
for i in range(n):
    temp = b[i]
    res += bisect_left(a, temp) * (n - bisect_right(c, temp))
    
print(res)