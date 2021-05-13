import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a,b = map(int,input().split())

g = gcd(a,b)
f = factorization(g)
ans = 1

for i,j in f:
  if i == 1:
    continue
  ans += 1

print(ans)