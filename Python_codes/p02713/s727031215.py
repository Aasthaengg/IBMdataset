import math

n = int(input())
ans = [math.gcd(i+1, math.gcd(j+1, k+1)) for i in range(n) for j in range(n) for k in range(n)]
print(sum(ans))