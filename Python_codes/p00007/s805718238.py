import math
n=int( input())
a=100000
for i in range(n):
    
    a+=a*0.05
    a=math.ceil(a/1000)*1000
   
print(math.floor(a))
