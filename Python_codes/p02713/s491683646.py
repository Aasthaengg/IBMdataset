import math
N = int(input())
 
sum = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        tmp = math.gcd(i,j)
        for k in range(1, N+1):
            sum += math.gcd(tmp, k)
 
print(sum)