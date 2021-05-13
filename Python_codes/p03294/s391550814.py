import numpy as np

N = int(input())
a = np.array(list(map(int, input().split())))

print(sum(a-1))