MOD=10**9+7
N=int(input())
A=list(map(int,input().split()))
res=1
cnt=[0]*3
for i in range(N):
    res=res*cnt.count(A[i])%MOD
    for j in range(3):
        if cnt[j]==A[i]:
            cnt[j]+=1
            break
print(res)