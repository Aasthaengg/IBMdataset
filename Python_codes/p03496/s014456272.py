import numpy as np
if __name__ == "__main__":
    N = int(input())
    A = [None]*N
    A = list(map(int, input().split()))
    flag_p = True
    max_a = max(A)
    max_idx = A.index(max_a)
    min_a = min(A)
    min_idx = A.index(min_a)
    if max_a < -min_a:
        flag_p = False
    
    print(N+N-1)
    
    if flag_p:
        #A = [a + max_a for a in A]
        for i in range(N):
            print(max_idx+1, i+1)
        
    else:
        #A = [a + min_a for a in A]
        for i in range(N):
            print(min_idx+1, i+1)

    if flag_p:
        for i in range(N-1):
            #A[i+1] += A[i]
            print(i+1, i+2)
    
    else:
        for i in range(N-1, 0, -1):
            #A[i-1] += A[i]
            print(i+1, i)