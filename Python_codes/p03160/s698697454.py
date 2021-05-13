import numpy as np
import sys
input = sys.stdin.readline # for speed up

n=int(input())
h=list(map(int,input().split()))

c=[0]*n

c[1]=c[0]+abs(h[1]-h[0])
for ii in range(2,n):
  c[ii]=min(c[ii-1]+abs(h[ii]-h[ii-1]),c[ii-2]+abs(h[ii]-h[ii-2]))

print(c[n-1])