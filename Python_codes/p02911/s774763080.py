import numpy as np

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

count = np.zeros(N)

for a in A:
    count[a-1] += 1

ans = K - (Q - count)

for answer in ans:
    if answer <= 0:
        print('No')
    else:
        print('Yes')
    
