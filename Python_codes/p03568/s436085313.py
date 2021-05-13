import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

tmp = (A%2==0).sum()

print(3**N - 2**tmp)