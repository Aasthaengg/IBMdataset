import numpy as np

N = input()
T,A = input().split()
H = input().split()

hoge = np.ndarray(int(N))
for piyo in range(int(N)):
  hoge[piyo] = int(H[piyo])

hoge = abs(int(T) - (0.006*hoge) - int(A))
print(np.argmin(hoge - int(A)) + 1)