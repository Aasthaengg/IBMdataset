n,k=map(int,input().split())
A = list(map(int,input().split()))
lA = len(A)
mod=10**9+7
cnt1=0
for i in range(lA):
    for j in range(i+1,lA):
        if A[i] > A[j]:
            cnt1+=1
cnt2=0
for i in range(lA):
    for j in range(lA):
        if A[i] > A[j]:
            cnt2+=1
print((cnt1*k+cnt2*(k*(k-1)//2))%mod)