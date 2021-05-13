import sys
import collections
import itertools

N,M = map(int,input().split())
array_2 = []
for I in range(N):
    array_2.append(input().split())
for I in array_2:
    del I[0]

array_2 = itertools.chain.from_iterable(array_2)
array_2 = collections.Counter(array_2)
count = 0
for I in array_2:
    if array_2[I] == N: count += 1
print(count)    