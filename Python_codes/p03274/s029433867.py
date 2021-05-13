import numpy as np

N, K = map(int, input().split(' '))
A = np.array(list(map(int, input().split(' '))))

if N == 1:
    print(abs(A[0]))
else:
    distances = np.array([0, *(A[1:] - A[:-1])])
    cumsum = distances.cumsum()
    to_left = abs(A[:-(K - 1)])
    to_right = abs(A[(K - 1):])
    to_start = np.minimum(to_left, to_right)
    to_goal = cumsum[(K - 1):] - cumsum[:-(K - 1)]

    print(min(to_start + to_goal))
