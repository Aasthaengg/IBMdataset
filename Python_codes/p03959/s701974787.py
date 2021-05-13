#CODEFESTIVAL2016qualC
N=int(input())
mod=10**9+7
T=list(map(int,input().split()))
A=list(map(int,input().split()))
ansT=[0]*N
ansA=[0]*N
ansT[0]=-1*T[0]
ansA[N-1]=-1*A[N-1]
for i in range(1,N):
    if T[i]>T[i-1]:
        ansT[i]=-1*T[i]
    else:
        ansT[i]=T[i]
    if A[N-1-i]>A[N-i]:
        ansA[N-1-i]=-1*A[N-1-i]
    else:
        ansA[N-1-i]=A[N-1-i]
ans=1
for i in range(N):
    if ansT[i]<0 and ansA[i]<0 and ansT[i]!=ansA[i]:
        ans=0
        break
    elif ansT[i]>0 and ansA[i]>0:
        ans=(ans*min(ansT[i],ansA[i]))%mod
    elif ansT[i]<0 and ansA[i]>0 and abs(ansT[i])>ansA[i]:
        ans=0
        break
    elif ansT[i]>0 and ansA[i]<0 and abs(ansA[i])>ansT[i]:
        ans=0
        break
print(ans)