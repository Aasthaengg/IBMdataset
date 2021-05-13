N, M = map(int, input().split())
As = list(map(lambda x: int(x)//2, input().split()))

from fractions import gcd
from math import ceil

cnt = 1
flg = True
while 1:
    num = 2**cnt
    lis = [1 if x%num==0 else 0 for x in As]
    s = sum(lis)
    if s==N:
        cnt+=1
        continue
    elif s==0:
        break
    else:
        flg = False
        break

if flg:
    lcm = As[0]
    for i in range(1, N):
        a = As[i]
        lcm = a*lcm//gcd(lcm, a)
    
    print(ceil((M//lcm)/2))
else:
    print(0)
