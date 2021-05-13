# coding: utf-8
# Your code here!

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

ans = sum(x>=k for x in l)
print(ans)