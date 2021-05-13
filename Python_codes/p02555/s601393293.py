S=int(input())

ss=len(str(S))

dp=[1 for _ in range(S+1)]
dp[0]=1
for i in range(0,min(S+1,3)):
    dp[i]=0
for i in range(3,min(S+1,10)):
    dp[i]=1

for i in range(3,S+1):
    for j in range(3,S+1):
        if(i+j<=S):
            #print(i,j)

            dp[i+j]=dp[i+j]+dp[i]
            dp[i+j]=dp[i+j]%(10**9+7)
            #print(dp[i+j])

print(dp[S])
#print(dp)
# dpp=[[0 for _ in range()] for _ in range(3)]
#print(dp)
# for i in range(S);
#     for j in range(li):
#         if(dp[j*k])
#         dp[j*k]=dp[j*k]=+1
#         for j in li:
#             if(j<=i):
#
#         dp[i]=dp[i-j]+1+dp[i]
# print(dp[S])
# print(dp)
# while()
