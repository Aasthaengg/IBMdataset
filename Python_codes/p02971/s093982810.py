from copy import deepcopy
n = int(input())
A = [int(input()) for i in range(n)]
A2 = deepcopy(A)
A2.sort()
for i in range(n):
    #print (A[i], A2[-1])
    if A[i] == A2[-1]:
        print (A2[-2])
    else:
        print (A2[-1])