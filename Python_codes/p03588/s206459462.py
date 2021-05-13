N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

M=max(B)
m=min(B)
for i in range(N):
    if B[i]==M:
        Mnum=A[i]
    if B[i]==m:
        mnum=A[i]

ans=mnum+m
print(ans)