import math
import time

n,k = map(int,input().split())

ans = 0
for i in range(1,n+1):
    if k<=i:
        ans +=1
    else:
        for j in range(1,1000):
            if i*(2**j)>=k :
                ans += 1/(2**j)
                break
print( ans/n )
