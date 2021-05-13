N=int(input())
A=list(map(int,input().split()))

import math
A_=list(set(A))

def lcm(a,b):
    gcd_= math.gcd(a,b)
    return int(a*b//gcd_)

lcm_ = A_[0]

for a_idx in range(1,len(A_)):
    lcm_ = lcm(lcm_,A_[a_idx])
    
lcm_ = lcm_-1
lcm_

ans=0
for a in A:
#     print(lcm_%a)
    ans+=lcm_%a
    
print(ans)