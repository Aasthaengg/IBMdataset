N,M=map(int,input().split())
A=list(map(int,input().split()))
S=[0]*(N+1)
for i in range(N):
    S[i+1]=S[i]+A[i]
num={}
for i in range(N+1):
    if S[i]%M in num:
        num[S[i]%M]+=1
    else:
        num[S[i]%M]=1
ans=0
for i in num.values():
    ans+=i*(i-1)//2
#print(num)
print(ans)
