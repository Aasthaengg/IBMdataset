import sys
 
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
 
import numpy as np
 
N = int(readline())
A = np.array(readline().split(), dtype=np.int64)
B = np.array(readline().split(), dtype=np.int64)
 
diff = A-B
lack = -diff[diff<0]
remain = diff[diff>0]
 
x = lack.sum()
remain.sort()
cum = remain[::-1].cumsum()
 
y = 0 if x == 0 else np.searchsorted(cum,x) + 1
 
answer = len(lack) + y if y <= len(remain) else -1
print(answer)