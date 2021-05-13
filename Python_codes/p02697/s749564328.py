import sys
import math
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
k = 0
j = 0
for i in range(m):
    if n%2==0 and ((n-j)-(i+1))*2<=n and k==0:
        j+=1
        k+=1
    print(i+1,n-j)
    j+=1