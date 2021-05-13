#!/usr/bin/env python3
(n,m,),*s=[[*map(int,i.split())]for i in open(0)]
s.sort()
ans = 0
for a,b in s:
    if m<1:
        break
    if m > b:
        ans += a*b
        m -= b
    else:
        ans += m*a
        m=0
print(ans)
