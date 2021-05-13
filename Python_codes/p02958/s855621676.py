import numpy as np

N = int(input())
P = list(map(int, input().split()))

before = np.array(P)
after = np.sort(before)
sort_cnt = np.count_nonzero(before - after)

print('YES' if sort_cnt <= 2 else 'NO')
