from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(Q)]

A_lst = combinations_with_replacement(range(1, M+1), N)
A_lst = list(map(list, A_lst))
A_lst.sort()

dm = 0 #d_sum_max
for A in A_lst:
    ds = 0 #d_sum
    for a, b, c, d in lst:
        if A[b-1] - A[a-1] == c:
            ds += d
    if ds > dm:
        dm = ds
print(dm)