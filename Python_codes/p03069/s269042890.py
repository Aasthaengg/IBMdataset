n=int(input())
s=input()
b=[0 for i in range(n)]
tmp=0
for i in range(n-1,-1,-1):
    if s[i]=="#":
        tmp+=1
    b[i]=tmp
w=[0 for i in range(n)]
tmp=0
for i in range(n):
    if s[i]==".":
        tmp+=1
    w[i]=tmp
tmp=0
ans=float("inf")
for i in range(n):
    tmp=n-(w[i]+b[i])
    if tmp<ans:
        ans=tmp
print(ans)