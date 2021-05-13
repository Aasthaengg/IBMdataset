_, *A = map(int, open(0).read().split())
lc = 10**6 + 1
C = [0] * lc
for a in A: C[a] += 1
import functools, math
t = any(sum(C[i::i]) > 1 for i in range(2, lc))
t += functools.reduce(math.gcd, A) > 1
print(['pairwise','setwise','not'][t], 'coprime')
