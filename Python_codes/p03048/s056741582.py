import math
import sys
r,g,b,n = map(int, input().split())
count=0
hiku=0
for i in range(n+1):
    for j in range(n+1):
        hiku=n-r*i-g*j
        if hiku%b==0 and hiku>=0:
            count+=1
print(count)