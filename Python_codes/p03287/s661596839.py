import collections
N, M = map(int, input().split())
A = [int(i) for i in input().split()]

Cum = [0 for _ in range(N+1)]
for i in range(N):
    Cum[i+1] = Cum[i]+A[i]

C = collections.Counter([x % M for x in Cum])

print(sum([x*(x-1)//2 for x in C.values()]))
