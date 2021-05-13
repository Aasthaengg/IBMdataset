# coding: utf-8
# Your code here!
n=int(input())
s=list(input())
ans=["A","B","C"]
count=0
for i in range(n-2):
    cnt=0
    for j in range(len(ans)):
        if s[i+j]==ans[j]:
            cnt+=1
    if cnt ==3:
        count+=1
print(count)