N=int(input())
S=str(input())
T=str(input())
mod=10**9+7
answer=1
if S[0]==T[0]:
  answer=3
else:
  answer=6
for i in range(1,N):
  if S[i]==T[i]:
    if S[i-1]==T[i-1]:
      answer=(answer*2)%mod
  else:
    if not S[i]==S[i-1]:
      if S[i-1]==T[i-1]:
        answer=(answer*2)%mod
      else:
        answer=(answer*3)%mod
print(answer)