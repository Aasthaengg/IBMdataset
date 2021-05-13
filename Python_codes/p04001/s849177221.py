s=input()
m=len(s)
sm=0
for i in range(2**(m-1)):
  a=list(str(bin(i)))[::-1]
  b=list(s)
  for j in range(len(a)-1,-1,-1):
    if a[j]=='1':
      b.insert(-j-1,'+')
  sm+=eval(''.join(b))
print(sm)