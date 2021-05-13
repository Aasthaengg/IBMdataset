import itertools
# import math
# import sys
# import numpy as np

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
H, W, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

cells = []
for i in range(H):
    cells.append(input())

rows = list(itertools.product((0,1), repeat=H))
columns = list(itertools.product((0,1), repeat=W))

def num_of_blacks(row, column):
    tot = 0
    for i in range(H):
        if row[i] == 0:
            continue
        for j in range(W):
            if column[j] == 0:
                continue
            if cells[i][j] == "#":
                tot += 1
    return tot

ans = 0
for row in rows:
    for column in columns:
        _ = num_of_blacks(row, column)
        if _ == K:
            ans += 1

print(ans)