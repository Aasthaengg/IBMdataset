#A
A=[1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
K=int(input())
print(A[K-1])

#C
if False:
    A,B,C=map(int,input().split())
    if 4*A*B<(C-A-B)**2:
        if C-A-B>=0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

#D
