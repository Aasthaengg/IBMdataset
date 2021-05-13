import numpy as np
N = int(input())
a = input().split()
a = np.array(a).astype(int)
count = 0
for i,ai in enumerate(a):
    
    if a[ai-1] == i+1:
        count = count + 1
print(count//2)