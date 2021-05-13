N = int(input())
B = list(map(int,input().split()))

import copy
A = copy.deepcopy(B)
for i in range(1,N-1):
    if B[i-1]<B[i]:
        A[i] = B[i-1]
        
A.append(B[-1])
print(sum(A))