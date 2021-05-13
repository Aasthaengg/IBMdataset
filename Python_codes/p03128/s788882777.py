N,M=map(int,input().split())
alist=list(map(int,input().split()))

blist=[False]*10
for a in alist:
  blist[a] = True

match=[6,2,5,5,4,5,6,3,7,6]
dp=[-1]*(N+1)

dp[0]=0
dp[1]=-1
for i in range(N+1):
  for j in range(1,10):
    if blist[j] and i+match[j]<=N:
      if dp[i+match[j]] < dp[i]+1:
        dp[i+match[j]] = dp[i]+1
#print(dp)

answer_str = ""
while(N>0):
  for i in reversed(range(1,10)):
    if blist[i] and N-match[i] >= 0 and dp[N-match[i]] == dp[N]-1:
      answer_str += str(i)
      N -= match[i]
      break
      
print(answer_str)