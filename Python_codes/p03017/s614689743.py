n,A,B,c,d=map(int,input().split())
s=input()
b=B-1
a=A-1
t=0
while t<2*n:
  if a!=c-1:
    if a+1<n and s[a+1]=='.' and a+1!=b:
      a+=1
    elif a+2<n and s[a+2]=='.' and a+2!=b and a+2<=c-1:
      a+=2
    else:
      if b+1<n and s[b+1]=='.' and b+1!=a:
        b+=1
      elif b+2<n and s[b+2]=='.' and b+2!=a and b+2<=d-1:
        b+=2
  else:
    if b!=d-1:
      if b+1<n and s[b+1]=='.' and b+1!=a:
        b+=1
      elif b+2<n and s[b+2]=='.' and b+2!=a and b+2<=d-1:
        b+=2
  t+=1
if a==c-1 and b==d-1:
  print('Yes')
else:
  print('No')