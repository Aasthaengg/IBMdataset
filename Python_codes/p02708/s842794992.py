import numpy

MOD = 10**9+7
N, K = [int(x) for x in input().split()]

cum = numpy.cumsum(range(N+1), dtype='int64')
count = 0

for i in range(K, N+1):
    min_num = cum[i-1]
    max_num = cum[-1] - cum[-i-1]

    count += (max_num - min_num + 1)
    count %= MOD

print(count + 1)
