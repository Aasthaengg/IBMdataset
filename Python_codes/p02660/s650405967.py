# coding: utf-8
# Your code here!
import bisect

line=[i*(i+1)//2 for i in range(10**6+1)]

N=int(input())


do=[0 for i in range(10**6+1)]

for i in range(2,int(N**0.5)+1):
    while N%i==0:
        N/=i
        do[i]+=1

ans=0 if N==1 else 1

for _,item in enumerate(do):
    index=(bisect.bisect_right(line,item))-1
    ans+=index

print(ans)


