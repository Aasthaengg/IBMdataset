import math
def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
n=int(input())
a=list(map(int,input().split()))
ans=computeGCD(a[0],a[1])
for i in range(2,n):
  ans=computeGCD(ans,a[i])
print(ans)