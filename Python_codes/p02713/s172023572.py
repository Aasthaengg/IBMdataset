import math
k = int(input())
sum = 0

for a in range(1,k+1):
    for b in range(1,k+1): 
        x = math.gcd(a, b)
        for c in range(1,k+1):
            sum += math.gcd(x, c)

print(sum)