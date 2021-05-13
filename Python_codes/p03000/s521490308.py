import itertools
N, X = map(int, input().split())
L = list(map(int, input().split()))
L = list(itertools.accumulate(L))
print(sum([i <= X for i in L]) + 1)