import sys
input = sys.stdin.readline

import fractions
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def mult_crt(b1,m1,b2,m2):
    gcd = xgcd(m1,m2)
    if b1 % gcd[0] != b2 % gcd[0]:
        return False
    else:
        x = b1 + m1*(b2-b1)//gcd[0]*gcd[1]
        m3 = (m1*m2) // fractions.gcd(m1,m2)
        b3 = x % m3
        return b3,m3

N,M = (int(x) for x in input().split())
a = list(map(int, input().split()))
temp = [a[0],a[0]//2]
broke = False
for i in range(1,N):
    bm = mult_crt(temp[1],temp[0],a[i]//2,a[i])
    if bm == False:
        broke = True
        break
    else:
        temp[0] = bm[1]
        temp[1] = bm[0]
if broke:
    print('0')
else:
    dm = divmod(M,temp[0])
    if dm[1] >= temp[1]:
        print(dm[0]+1)
    else:
        print(dm[0])