import numpy as np
from scipy import signal

H, W =map(int, input().split()) 
S = np.array([list(input()) for _ in range(H)])
K = np.array([[1,1,1],[1,0,1],[1,1,1]])
T = signal.convolve2d(S=="#",K,"same").astype(str)
T[S=="#"]="#"
for t in T:
    print("".join(t))