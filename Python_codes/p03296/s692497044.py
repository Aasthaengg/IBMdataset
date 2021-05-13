from itertools import groupby

N, *A = map(int, open(0).read().split())
print(sum(len(tuple(v)) // 2 for _, v in groupby(A)))
