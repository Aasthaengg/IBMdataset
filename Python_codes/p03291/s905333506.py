s=input()
mod=10**9+7
n,a,b,c=1,0,0,0
for i in s:
  if i=="A":
    a+=n
  if i=="B":
    b+=a
  if i=="C":
    c+=b
  if i=="?":
    n,a,b,c=3*n,3*a+n,3*b+a,3*c+b
  n%=mod
  a%=mod
  b%=mod
  c%=mod
print(c)