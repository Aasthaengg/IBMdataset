N=int(input())
S=input()
if S=='#'*N or S=='.'*N:
  print(0)
  exit()
rightB=0
for i in S:
  if i=='#':
    rightB+=1
rightW=N-rightB
leftB=0
leftW=0
ans=min(rightB,rightW)
for i in range(N):
  if S[i]=='.':
    leftW+=1
    rightW-=1
    d=rightW+leftB
    ans=min(ans,d)
  else:
    leftB+=1
    rightB-=1
    d=rightW+leftB
    ans=min(ans,d)
print(ans)