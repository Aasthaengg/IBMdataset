import math

n = int(input())
a = list(map(int,input().split()))
ans = 0

for i in range(1,n):
    if i == 1:
        ans = math.gcd(a[0],a[i])
    else:
        ans = math.gcd(ans,a[i])

print(ans)
