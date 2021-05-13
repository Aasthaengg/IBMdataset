N=int(input())
S=list(str(input()))
c=0
ans=0
for i in range(N):
  if S[i]=="I":
    c+=1
  else:
    c-=1
  if c>ans:
    ans=c
print(ans)
  
