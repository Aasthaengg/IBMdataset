from math import gcd

A, B = map(int, input().split())

m = gcd(A, B)
#print(m)

num = int(m**0.5) #mに対する素因数分解は、int(√m)の場合を調べればよい
ans = 1

for i in range(2,num+1):
    if m%i:
        continue
    ans += 1
    while not m%i:
        m /= i

if m>1:
    ans+=1 #m+1が素因数の場合がある

print(ans)