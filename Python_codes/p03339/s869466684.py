n=int(input())
s=input()
x=[0]*n
t=0
for i in range(n):
    if s[i]=="E":
        t+=1
    x[i]=t
M=x[n-1]
c=0
ans=10**9
for i in range(n):
    ans=min(ans,i-c+M-x[i])
    c=x[i]
print(ans)