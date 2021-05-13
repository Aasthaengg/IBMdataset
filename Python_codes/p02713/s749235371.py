import math
a = int(input())
lis =[]
ans = 0
for x in range(1,a+1):
    for y in range(1, a+1):
        lis.append(math.gcd(x,y))
for z in range(1, a+1):
    for l in lis:
        ans += math.gcd(z,l)
print(ans)