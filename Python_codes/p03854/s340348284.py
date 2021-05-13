
S=input()

N=len(S)
dp=[0]*(N+1)
dp[0]=1
L=["dream", "dreamer", "erase", "eraser"]
for i in range(1,N+1):
    for l in L:
        n=len(l)
        if 0<=i-n<N:
            if S[i-n:i]==l and dp[i-n]:
                dp[i]=1

if dp[-1]:
    print("YES")
else:
    print("NO")