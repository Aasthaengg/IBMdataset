import copy
import numpy as np
n=int(input())
xl=[]
for i in range(n):
    x,l = map(int,input().split())
    xl.append([x-l,l+x])
#print(xl)
xl = sorted(xl, key=lambda x: x[0],reverse=True)
#print(xl)

ans=0
r=2*(10**9+1)
for i in range(n):
  if xl[i][1]>r:
    continue
  if xl[i][0]<=r:
    r=xl[i][0]
    #print("r",r)
    ans+=1
print(ans)