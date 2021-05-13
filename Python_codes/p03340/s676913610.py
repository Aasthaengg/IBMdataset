def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ret = N
    i = 0
    xor_A = A[0]
    j = 1
    while i < N-1:
        tail_flag = False
        # next_i = i+1
        if i == j:
            xor_A = A[i]
            j = i+1
        while j < N:
            if xor_A ^ A[j] == xor_A+A[j]:
                tail_flag = True
                # print(i,j, xor_A, xor_A^A[j], xor_A+A[j])
                xor_A = xor_A ^ A[j]
                ret += j-i
            else: 
                tail_flag = False
                break
            
            if j != N-1: 
                j += 1
            else: break
        
        xor_A ^= A[i]
        i += 1
        if tail_flag and j == N-1: break
                
    print(ret)
    
solve()