n=int(input())
s=input()
r,g,b=[],[],[]
for i in range(n):
  if s[i]=='R':
    r+=[i+1]
  elif s[i]=='G':
    g+=[i+1]
  elif s[i]=='B':
    b+=[i+1]

ans=len(r)*len(g)*len(b)

for i in range(n-2):
  for dist in range(1,(n-i+1)//2):
    if s[i]!=s[i+dist] and s[i]!=s[i+dist*2] and s[i+dist]!=s[i+dist*2]:
      ans-=1
      

print(ans)