import math

n = int(input())
t = []
for i in range(n):
    p = int(input())
    t.append(p)

ans = t[0]

for i in range(1,n):
    ans = (ans*t[i]) // math.gcd(ans,t[i])

print(ans)