# coding: utf-8

(N, M) = map(int, input().split(" "))

ids = list(range(1, N+1))

L_max = 0
R_min = 10000000000000000000
for _ in range(M):
    (L, R) = map(int, input().split(" "))
    if L > L_max:
        L_max = L
    if R < R_min:
        R_min = R

ids = [i for i in ids if L_max <= i <= R_min]
print(len(ids))
