a,b=map(int,input().split())
import math
c= math.gcd(a,b)
c2=c
l=[]
i=2
while i<=c:
  if c % i==0:
    c=c//i
   
    l.append(i)
  else:
    i+=1
  if i*i-1>c:
    l.append(c)
    break
  
print(len(set(l))+1)
