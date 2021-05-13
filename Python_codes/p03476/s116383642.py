import numpy as np
MAXX = 10**5 + 5

isprime = np.ones(MAXX, dtype=bool)
count = np.zeros(MAXX, dtype=int)

#eratosen no furui
isprime[0] = isprime[1] = False
for i in range(2, MAXX):
    if isprime[i]:
        isprime[2*i::i] = False

for i in range(1, MAXX):
    if isprime[i] and isprime[(i+1)>>1]:
        count[i] = 1

#累積和
for i in range(1, MAXX):
    count[i] += count[i-1]

#read query
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(count[r] - count[l-1])



