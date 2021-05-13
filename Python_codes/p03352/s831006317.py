import math
X=int(input())
a=math.sqrt(X)
b=int(a)
ans=1
for i in range (2,b+1):
    for j in range(2,10):
        if i**j <=X <i**(j+1):
            ans=max(ans,i**j)
            break

print(ans)