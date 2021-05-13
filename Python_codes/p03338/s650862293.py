N=int(input())
S=input()
ans=0
for i in range(1,N):
  temp=0
  check1=set(S[:i])
  check2=set(S[i:])
  for s in check1:
    if s in check2:
      temp+=1
  ans=max(ans,temp)
print(ans)
