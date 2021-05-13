N,K=map(int,input().split())
A=list(map(int,input().split()))
MOD=10**9+7
count1=0
count2=0
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if A[i]>A[j]:
            if i<j:
                count1+=1
            else:
                count2+=1
ans=count1*K*(K+1)//2%MOD
ans=ans+count2*(K)*(K-1)//2
print(ans%MOD)