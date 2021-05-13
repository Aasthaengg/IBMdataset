import numpy as np

N, K = input().split(" ")
N, K = int(N), int(K)

S = np.array(list(input()), dtype='U1')
 
x = np.sum(S[1:] == S[:-1])
 
x += 2*K
x = min(x, N-1)
print(x)