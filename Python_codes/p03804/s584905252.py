N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

import numpy as np
A = np.array(A)
B = np.array(B)
# print(A)
# print()
# print(B)
# print()

if N==M:
    if np.all(A==B):
        print('Yes')
    else:
        print('No')
else:
    for i in range(N-M):
        for j in range(N-M):
    #         print(i,j)
            a = A[i: i+M, j: j+M]
    #         print(a)
    #         print()
            if np.all(a == B):
                print('Yes')
                break
        else:
            continue
        break
    else:
        print('No')