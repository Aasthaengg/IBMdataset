import itertools
import collections
import math

N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

def cmb(n,r):
    if n < 0 or r < 0 or n-r < 0:
        return 0
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

sumA = list(itertools.accumulate(A))
sumA = [0]+[i % M for i in sumA] 
c = collections.Counter(sumA)
lsA = c.most_common()
ans = 0

for i in lsA:
    ans += cmb(i[1],2)

print(ans)