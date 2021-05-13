N,K=map(int,input().split())
S=[int(i) for i in input().split()]

dp=[False]*(K+1)

for i in range(K+1):
    #print(dp)
    for s in S:
        f=False
        if i-s<0:
            break
        if not dp[i-s]:
            dp[i]=True
            break
#print(dp)
if dp[-1]:
    print("First")
else:
    print("Second")