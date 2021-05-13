n=int(input())
ans=0
a=[0]*n
b=[0]*n
for i in range(n):
  s=input()
  ans+=s.count('AB')
  if s[-1]=='A':a[i]=1
  if s[0]=='B':b[i]=1
m=min(sum(a),sum(b))
ans+=m
if m:
  for i,j in zip(a,b):
    if i+j and i*j==0:break
  else:ans-=1
print(ans)