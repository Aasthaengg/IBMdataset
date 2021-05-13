prime = [1]*(100001)
prime[0] = 0
prime[1] = 0
for i in range(2,100001):
    if prime[i]:
        for j in range(i*i,100001,i):
            prime[j] = 0

for i in range(100000,-1,-1):
    if prime[i]:
        if prime[(i+1)//2] != 1:
            prime[i] = 0

from itertools import accumulate
accum = list(accumulate(prime))

Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    print(accum[r]-accum[l-1])
