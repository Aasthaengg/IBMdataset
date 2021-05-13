n,m=map(int,input().split())
s={1,m}
for i in range(2,int(m**0.5)+1):
  if m%i<1: s|={i,m//i}
for i in sorted(s):
  if i*n>m: break
  a=i
print(a)