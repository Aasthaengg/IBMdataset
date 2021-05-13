import math
n = int(input())
x = list(map(int,input().split(" ")))
a=math.ceil(sum(x)/n)
s = sum((xx - a)**2 for xx in x)
tmp = s
a = a-1
s = sum((xx - a)**2 for xx in x)
if s > tmp:
    print(tmp)
else:
    print(s)