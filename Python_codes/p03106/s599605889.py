import math
a,b,k = map(int,input().split())

g = math.gcd(a,b)
c = 0
i = 1
for i in range(g,0,-1) :
    if g%i == 0 :
        c+=1
        if c==k :
            break
print(i)     
    
