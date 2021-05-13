n=int(input())
l=[]
while n!=1 and n!=0:
  l.append(abs(n)%2)
  if n>0:
    n=-n
    n//=(-2)
    n=-n
  elif n<0:
    n=abs(n)
    n//=(-2)
    n=-n
l.append(n)
l=l[::-1]
ans=str()
for i in l:
  ans+=str(i)
print(ans)
