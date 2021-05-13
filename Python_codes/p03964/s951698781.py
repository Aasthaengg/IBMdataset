n=int(input())
lists=[]
import math
for i in range(n):
    a,t=map(int,input().split())
    lists.append([a,t])
x=1
y=1
for i in range(n):
    j=max((x-1)//lists[i][0]+1,(y-1)//lists[i][1]+1)
    x=lists[i][0]*j
    y=lists[i][1]*j
print(x+y)