import numpy as np

N = int(input()) 
H = list(map(int, input().split()))

def count(b):
    b = np.clip(b, 0, 1)
    return int(b[0] > 0) + np.sum(np.diff(b) > 0)

heights = np.array(H)

cnts = []
for water in range(100):
    arr = np.clip(heights - water, 0, 101)
    cnts.append(count(arr))

print(np.sum(cnts))