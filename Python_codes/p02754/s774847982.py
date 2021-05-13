n,a,b=map(int,input().split())
s=int(n/(a+b))*a
if n%(a+b)>=a:
  s+=a
else:
  s+=n%(a+b)
print(s)