import math as math
n = int(input())
li = [1]
nroot = int(math.sqrt(n))
for i in range(2,nroot+1):
    for j in range(2,100):
        if i**j <= n:
            li.append(i**j)
        else:
            break
print(max(li))