# from itertools import accumulate
import itertools

N, x, *A = map(int, open(0).read().split())

B = list(itertools.accumulate(sorted(A))) # cumsum
C = list(itertools.accumulate(sorted(A, reverse=True))) # cumsum

if B[-1] == x:
    print(len(A))
elif B[-1] < x:
    x -= B[-1]
    print(N - (len(list(itertools.takewhile(lambda e: e <= x, C))) + 1))
elif x < B[-1]:
    print(len(list(itertools.takewhile(lambda e: e <= x, B))))