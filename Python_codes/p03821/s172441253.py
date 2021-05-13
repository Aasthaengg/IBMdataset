# A - Multiple Array
import numpy as np

N = int(input())
A = np.zeros(N, dtype=int)
B = np.zeros(N, dtype=int)
ans = 0

for i in range(N):
    A[i], B[i] = map(int, input().split())
for i in range(1,N+1):
    tmp = -(A[N-i] + ans) % B[N-i]
    ans += tmp
    
print(ans)