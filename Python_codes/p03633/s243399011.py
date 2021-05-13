import math
n=int(input())
ans=int(input())
for i in range(n-1):
    t=int(input())
    ans=(t*ans)//(math.gcd(t,ans))
print(ans)
