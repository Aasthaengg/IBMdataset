# import itertools
# import math
# import sys
# import numpy as np

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# H, W, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# S = input()

# d = sorted(d, reverse=True, key=lambda x:x[0])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

data = []
for i in range(N):
    data.append(list(map(int, input().split())))
data = sorted(data, reverse=True, key=lambda x:x[2])

ans_x = 0
ans_y = 0
ans_h = 0
for i in range(101):
    for j in range(101):
        H = -1
        for l in data:
            if H == -1:
                _ = l[2] + abs(l[0] - i) + abs(l[1] - j)
                H = _
            else:
                h_i_cal = max(H - abs(l[0] - i) - abs(l[1] - j), 0)
                if h_i_cal != l[2]:
                    break
        else:
            ans_x = i
            ans_y = j
            ans_h = H

print(ans_x, ans_y, ans_h)
