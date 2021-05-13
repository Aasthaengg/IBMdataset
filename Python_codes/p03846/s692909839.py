# coding: utf-8
N=int(input())
A=list(map(int,input().split()))
A.sort()

MOD=10**9+7
flg=True
k=1

if N%2==1:
    k=2
    a=A.pop(0)
    if a!=0:
        flg=False
        
for i in range(N//2):
    if A[i*2]!=k or A[i*2+1]!=k:
        flg=False
    k+=2
    
if flg:
    ans=1
    for i in range(N//2):
        ans*=2
        ans=ans%MOD
else:
    ans=0

print(ans)

