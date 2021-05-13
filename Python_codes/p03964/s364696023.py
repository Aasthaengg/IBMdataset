from math import ceil
 
n = int(input())
a = 1
b = 1
 
for i in range(n):
    s,t = map(int,input().split())
    #x = max([ceil(a/s), ceil(b/t)])
    x = max((a+s-1)//s, (b+t-1)//t)

 
    a = x*s
    b = x*t

print(a+b)