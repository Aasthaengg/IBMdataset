S=list(input())
cnt=0
ans=0
for i in range(len(S)-1,-1,-1):
  if S[i]=='W':
    cnt+=1
  else:
    ans+=cnt

print(ans)