import numpy as np

N = int(input())
time_array = np.array([int(input()) for _ in range(5)])
N_array = np.ones(5, dtype=np.int)*N

count_array = np.ceil(N_array / time_array)
answer = int(count_array.max() + 4)

print(answer)
