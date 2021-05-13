S=input()
dp=[0]*len(S)
a=0
for i in range(len(S)):
  if S[i]=='R':
    a+=1
  else:
    dp[i]+=a//2
    dp[i-1]+=a-a//2
    a=0
for i in range(len(S)-1,-1,-1):
  if S[i]=='L':
    a+=1
  else:
    dp[i]+=a//2
    dp[i+1]+=a-a//2
    a=0
print(*dp)