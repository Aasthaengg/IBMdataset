import numpy as np
n = int(input())
f = np.array(list(map(int, input().split())) )
print(np.where(abs(f - np.mean(f)) == min(abs(f - np.mean(f))))[0][0])