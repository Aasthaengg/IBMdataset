[A, B, C, K] = [int(i) for i in input().split()]

j1 = A - K
j2 = A + B - K
if j2 >0: # K < A + B
    if j1 < 0: #A > K
        print(A)
    else:
        print(K)
else:
    print(A + j2)