import numpy as np
N = int(input())
A = np.array([0] + [int(x) for x in input().split()] + [0])
total = np.abs(np.diff(A)).sum()
saved = np.abs(A[1:-1]-A[:-2])+np.abs(A[1:-1]-A[2:])-np.abs(A[:-2]-A[2:])
answer = total - saved
print(*answer, sep='\n')
