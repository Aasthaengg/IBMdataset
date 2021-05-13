n=int(input())
import math

i=2
l=0
k=int(math.sqrt(n))+1
s=[0]*k
while i<k:
    if s[i]==0:
        z=i
        while n%z==0:
            n//=z
            #print(z,n)
            z*=i
            l+=1
        while n%i==0:
            n//=i
            
            
    for j in range(i,k,i):
        s[j]=1
    i+=1
if n>1:
    r=0
    for i in range(2,k):
        if n%i==0:
            r=1
            break
    if r==0:
        l+=1
print(l)