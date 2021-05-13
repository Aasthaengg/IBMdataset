import itertools
from collections import defaultdict

N ,K = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + [x-1 for x in A]

Acum = list(itertools.accumulate(A))
Acum = [x % K for x in Acum]

counter = defaultdict(int)
answer = 0
for i,x in enumerate(Acum):
    answer += counter[x]
    counter[x] += 1
    if i >= K-1:
        counter[Acum[i-K+1]] -= 1

print(answer)