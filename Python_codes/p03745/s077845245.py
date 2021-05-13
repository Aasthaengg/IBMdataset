import numpy as np
N = int(input())
A = list(map(int, input().split()))

turn_p = 0
if N > 2:
    a_ = A[1]
    d_ = np.sign(A[1] - A[0])
    for a in A[2:]:
        d = np.sign(a - a_)
        #print(a, d, d_, turn_p)
        if d != 0:
            if d_ == 0:
                d_ = d
            elif d_ != d:
                turn_p += 1
                d_ = 0
        a_ = a 

print(turn_p+1)
    

