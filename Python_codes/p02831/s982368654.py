import math 

a,b = map(int,input().split())

x = math.gcd(a,b)
y = a * b
ans = y // x
print(ans)
