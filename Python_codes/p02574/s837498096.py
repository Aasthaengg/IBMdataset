from collections import defaultdict
MAX_A = 10**6

sieve = [[] for _ in range(MAX_A+1)]
# sieve[i] = True if i is prime
# sieve[i] = prime factors of i

for f in range(2, MAX_A + 1):
  if not sieve[f]:
    c = f
    while c <= MAX_A:
      sieve[c].append(f)
      c += f

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
  for s in sieve[a]:
    cnt[s] += 1

def is_pairwise_coprime():
  return all(v == 1 for v in cnt.values())

def is_setwise_coprime():
  return all(v < N for v in cnt.values())

if is_pairwise_coprime():
  print('pairwise coprime')
elif is_setwise_coprime():
  print('setwise coprime')
else:
  print('not coprime')
