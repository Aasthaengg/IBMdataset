n=input()
z=[0]*(n+1)
z[0]=1
for i in xrange(1,n+1):
  s=0
  if i-3>=0:
    s=z[i-3]
  z[i]=(z[i-1]+s)%(pow(10,9)+7)
print (z[-1]-z[-2])%(pow(10,9)+7)