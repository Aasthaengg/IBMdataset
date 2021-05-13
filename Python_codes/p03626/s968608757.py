N = int(input())
S1 = list(input())
S2 = list(input())
cnt= 0
ans = 0
flag= 0
while cnt<N:
  if S1[cnt]==S2[cnt]:
    if cnt==0:
      ans+=3
    elif flag==1:
      ans*=2
    elif flag==2:
      ans*=1
    flag=1
    cnt+=1
  elif S1[cnt]!=S2[cnt]:
    if cnt==0:
      ans +=6
    elif flag==1:
      ans*=2
    elif flag==2:
      ans*=3
    flag=2
    cnt+=2
  ans %=(10**9+7)
print(ans)