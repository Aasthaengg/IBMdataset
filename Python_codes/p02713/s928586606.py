import math
k=int(input())
ans= 0
for s in range(1,k+1):
    for t in range(1,k+1):
        if math.gcd(s,t) == 1:
            ans=ans+k
        else:
            for u in range(1,k+1):
                ans= ans + math.gcd(math.gcd(s,t),u)
print(ans)