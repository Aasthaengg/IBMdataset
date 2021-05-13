import sys
import numpy as np

read = sys.stdin.read

n = int(input())
p = np.array(read().split(), dtype=np.int64).reshape(-1,2)

ans = np.sum((p[:,1]-p[:,0])+1)
print(ans)