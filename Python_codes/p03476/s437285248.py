import sys


Q = int(input())
pair = []

MAX = 0
for i in range(Q):
    l, r = map(int, input().split())
    MAX = max(MAX, l, r)
    pair.append((l, r))

N = 101010
N = 25
N = MAX + 1
is_prime = [1 for i in range(N)]

is_prime[0] = is_prime[1] = 0

# sieve
for i in range(2, N):
    if not is_prime[i]:
        # 0, 1, 4, 6, 9, ...
        continue
    for j in range(i*2, N, i):
        #print(j)
        is_prime[j] = 0
#print('sieve')
#print(is_prime)

# 2017-like
a = [0 for i in range(N)]
for i in range(N):
    if i % 2 == 0:
        continue
    if is_prime[i] and is_prime[(i+1) // 2]:
        a[i] = 1
#print('2017')
#print(a)

# accum
s = [0]
for i, n in enumerate(a):
    s.append(s[i] + n)
s.pop(0)
#print('accum')
#print(s)

# Query
#print(pair)
#print('ANS')
for l, r in pair:
    print(s[r] - s[l-1])

