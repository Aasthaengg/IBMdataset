N=int(input())
S=input()
check=0
ans=0
for i in range(0,N):
  if S[i]=="I":
    check+=1
  else:
    check-=1
  ans=max(ans,check);
print(ans)
