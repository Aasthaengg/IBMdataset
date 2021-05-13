from math import sqrt, ceil
from collections import defaultdict
def prime(N):
    temp = [True]*(N+1)
    temp[0] = temp[1] = False
    for i in range(2, ceil(sqrt(N+1))):
        if temp[i]:
            temp[i+i::i] = [False]*(len(temp[i+i::i]))                            
    primes = [ n for n in range(N+1) if temp[n] ]
    return primes
n = int(input())
dic = defaultdict(lambda:0)
p = prime(n)
for i in range(1,n+1):
    for j in p:
        while i % j == 0:
            i //= j
            dic[j] += 1
        if i == 1:
            break
a = 0 #75
b = 0 #25
c = 0 #15
d = 0 #5
e = 0 #3
for i in dic.keys():
    if dic[i] >= 74:
        a += 1
    if dic[i] >= 24:
        b += 1
    if dic[i] >= 14:
        c += 1
    if dic[i] >= 4:
        d += 1
    if dic[i] >= 2:
        e += 1
ans = 0
ans += a
ans += b*(e-1)
ans += c*(d-1)
ans += d*(d-1)*(e-2)//2
print(ans)