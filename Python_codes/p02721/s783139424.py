# coding: utf-8
# Your code here!
MI=lambda:map(int,input().split())
n,k,c=MI()
s=input()

left=[];right=[]
i=0
while 0<=i<=n-1:
    if s[i]=="o":
        left+=(i),
        i+=c+1
    else:
        i+=1
j=n-1
while 0<=j<=n-1:
    if s[j]=="o":
        right+=j,
        j-=(c+1)
    else:
        j-=1

ans=list(set(left)&set(right))

if len(ans)>k:
    print()
else:
    for q in sorted(ans):
        print(q+1)