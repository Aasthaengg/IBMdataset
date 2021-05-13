# coding: utf-8
# Your code here!
import bisect

N=int(input())

A=list(map(int,input().split()))

A.sort()

sum_A=[]
for item in A:
    if sum_A:
        sum_A.append(sum_A[-1]+item)
    else:
        sum_A.append(item)

ans=0
for i in range(len(A)):
    while i!=len(A):
        index=bisect.bisect_right(A,2*sum_A[i])-1
        if i==index:
            break
        else:
            i=index
    if i==len(A)-1:
        ans+=1

print(ans)