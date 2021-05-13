n = int(input())
a = list(map(int , input().split()))

import fractions
lcm = a[0]
for ai in a:
    lcm = lcm * ai // fractions.gcd(lcm, ai)
    #lcm =  fractions.gcd(lcm, ai)
ans = 0
for ai in a:
    ans += (lcm-1)%ai
print(ans)
