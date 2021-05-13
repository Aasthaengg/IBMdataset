import math

n=int(input())
t=int(input())
mint=t
t1=int(input())
if t1<t: mint=t1
maxtt=t1-t

for i in range(2,n):
    t=int(input())

    if t-mint>maxtt: maxtt=t-mint
    if t<mint: mint=t

print(int(maxtt))
