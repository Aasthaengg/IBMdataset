import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

l = list(itertools.permutations(range(1,N+1)))
tp = tuple(P)
tq = tuple(Q)
tpi = l.index(tp)
tqi = l.index(tq)
print(abs(tpi-tqi))