import numpy as np
N = int(input())
transport = [int(input()) for _ in range(5)]
print(int(np.ceil(N / np.min(transport))) + 4)