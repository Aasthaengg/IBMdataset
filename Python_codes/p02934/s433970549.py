import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

answer = np.sum(1/A)
print(1/answer)