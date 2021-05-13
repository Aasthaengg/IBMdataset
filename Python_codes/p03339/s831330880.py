n=int(input())
A=[0]*n
S=input()

for i in range(n):
    if S[i]=="E":
        A[i]=1
E=sum(A)
e=E

ans=n+10
for i in range(n):
    if A[i]==1:
        e-=1
        ans=min(e+i-(E-e-1),ans)
    else:
        ans=min(e+i-(E-e),ans)
print(ans)