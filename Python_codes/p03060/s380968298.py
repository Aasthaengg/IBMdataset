import numpy as np

N = int(input())
V = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))
ans = V - C

print(sum([i for i in ans if i >= 0]))