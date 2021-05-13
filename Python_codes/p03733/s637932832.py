import numpy as np
N, T = map(int, input().split())
t = list(map(int, input().split()))
timer = np.zeros(N)

for i in range(1, N):
    if t[i] - t[i-1] >= T:
        timer[i] = t[i] - t[i-1]
    else:
        timer[i] = T

timer = timer - T
timer[0] = 0


print(int(t[-1]+T - sum(timer)))
