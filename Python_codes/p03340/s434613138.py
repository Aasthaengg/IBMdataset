import sys
import math
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
n=int(input())
a=list(map(int,input().split()))
cnt=0
i=0
j=0
tmp=0
while(i<n):
    while(j<n):
        if tmp&a[j]==0:
            tmp+=a[j]
            cnt+=j-i+1
            # print(str(i)+" "+str(j))
        else:
            break
        j+=1
    tmp^=a[i]
    i+=1
print(cnt)