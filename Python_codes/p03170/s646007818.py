N,K=map(int,input().split())
#N=int(input())
A=list(map(int,input().split()))
#p=10**9+7
ma=[]
dp=[False]*(K+1)

for i in range(1,K+1):
    if i in A:
        dp[i]=True
    for j in A:
        if i < j:
            continue
        elif not dp[i-j]:
            dp[i] = True

#print(dp)
if dp[K]:
    print("First")
else:
    print("Second")


