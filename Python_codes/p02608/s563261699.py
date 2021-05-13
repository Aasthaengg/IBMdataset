from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
ans = [0 for i in range(n)]

tmp=0
for i in range(1,math.ceil(math.sqrt(n))):
    for j in range(1,math.ceil(math.sqrt(n))):
        for k in range(1,math.ceil(math.sqrt(n))):
            tmp = i**2+j**2+k**2+i*j+j*k+k*i
            if tmp <=n:
                ans[tmp-1]+=1

for i in range(0,n):
    print(ans[i])