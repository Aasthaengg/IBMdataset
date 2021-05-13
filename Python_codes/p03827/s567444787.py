n=int(input())
S=input()
crt=0
ans=0
for s in S:
  if s=="I":
    crt+=1
  else:
    crt-=1
  ans=max(ans,crt)
print(ans)