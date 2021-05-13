n=int(input())
a=0
b=0
ab=0
x=0
for i in range(n):
  s=input()
  l=len(s)-1
  if s[0]=='B':
    if s[l]=='A':
      ab+=1
    else:
      b+=1
  elif s[l]=='A':
    a+=1
  x+=s.count('AB')
if ab>0:
  x+=ab-1
  x+=(a>0)+(b>0)
  a-=1;b-=1
a=max(0,a);b=max(0,b)
x+=min(a,b)
print(x)