import numpy as np

N = int(input())

Ns = [i for i in range(1,N+1)]

counts = []
for N in Ns:
    count = 0
    while N % 2 == 0:
        N //= 2
        count += 1
    counts.append(count)

print(Ns[np.argmax(counts)])