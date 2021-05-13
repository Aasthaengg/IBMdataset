# coding: utf-8
# Your code here!

N,K=map(int,input().split())
H=list(map(int,input().split()))

ans=0
for i in range(K):
    ans+=H.count(i)

print(N-ans)