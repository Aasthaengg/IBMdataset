def gcd(x,y):
   if x<=y:
     tmp=x
     x=y
     y=tmp
   r=x%y
   while(r!=0):
     x=y
     y=r
     r=x%y
   return y
a=input().split()
b=[int(i) for i in a]
print(gcd(b[0],b[1]))

