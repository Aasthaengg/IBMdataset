n=int(input())
s=input()
ans=10**9
w=[0]*n
b=[0]*n
cw,cb=0,0
for i in range(n):
  if s[i]==".":
    cw+=1
  else:
    cb+=1
  w[i]=cw
  b[i]=cb

for i in range(n):
  ans=min(ans,b[i]+w[-1]-w[i])
ans=min(ans,b[-1],w[-1])
print(ans)
