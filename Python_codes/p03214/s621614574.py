import math
from statistics import mean
# a=int(input())
b=int(input())
# c=[]
# for i in b:
#     c.append(i)
#e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(3)]

mea = mean(f)
lis=[]

if mea in f :
    print(f.index(mea))
else:
    for i in range(len(f)):
        lis.append(abs(mea-f[i]))
    print(lis.index(min(lis)))