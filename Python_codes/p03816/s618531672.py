# coding: utf-8
import collections

N=int(input())
A=list(map(int,input().split()))

C=collections.Counter(A)

d=0

sA=list(set(A))

for i in range(len(C)):
    d+=C[sA[i]]-1

eat_num=-(-d//2)

ans=N-eat_num*2

print(ans)