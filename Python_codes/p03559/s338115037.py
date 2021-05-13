from bisect import *
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
c.sort()
res = 0
for i in b:
    temp_a = bisect_left(a, i)
    temp_c = n - bisect_right(c, i)
    res += temp_a*temp_c
print(res)