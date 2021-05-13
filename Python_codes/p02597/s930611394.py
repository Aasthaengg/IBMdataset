N=int(input())
S=input()
ans=0
i=0
j=N-1
while i<j:
  while i<N:
    if S[i]=='W':
      break
    else:
      i+=1
  while j>0:
    if S[j]=='R':
      break
    else:
      j-=1
  if i<j:
    ans+=1
    i+=1
    j-=1
print(ans)