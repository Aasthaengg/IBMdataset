a,b,c,d=map(int,input().split())
nc=(b//c)-((a-1)//c)
nd=(b//d)-((a-1)//d)

import math
p=math.gcd(c,d)
q=(c*d)//p

ncd=(b//q)-((a-1)//q)
r=nc+nd-ncd
ans=(b-a+1)-r
print(ans)