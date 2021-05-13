import sys

n,m=map(int,input().split())
ans=[0]*(m+1)
output=0

for i in range(n):
    k=list(map(int,input().split()))
    for j in range(1,len(k)):
        ans[k[j]]+=1

for i in ans:
    if i==n:
        output+=1

print(output)