n,*a=map(int,open(0).read().split())
x=s=l=c=0
for r,b in enumerate(a):
  x^=b
  s+=b
  while x<s:
    x^=a[l]
    s-=a[l]
    l+=1
  c+=r-l+1
print(c)
