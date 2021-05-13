import numpy as np

n = int(input().strip())
A = list(map(int,input().strip().split(' ')))
sorted_A = sorted(A)
ai=sorted_A[-1]
print(ai)
del sorted_A[-1]
tmplist=np.array([min(i,ai-i) for i in sorted_A])
maxidx = np.argmax(tmplist)

print(sorted_A[int(maxidx)])
