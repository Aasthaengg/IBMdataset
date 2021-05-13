# coding: utf-8
# Your code here!
N=int(input())
S=list(input())

ans=0
log=[1]*26
for item in S:
    item=ord(item)-97
    log[item]+=1

ans=1
for item in log:
    ans*=max(item,1)

print((ans-1)%(10**9+7))