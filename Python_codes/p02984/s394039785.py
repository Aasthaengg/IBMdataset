def solve():
    N = int(input())
    A = list(map(int, input().split()))
    sum_even_A = sum(A[::2])
    B = [sum(A)-2*sum(A[1::2])]
    for i in range(1,N):
        B.append(2*A[i-1]-B[i-1])
        
    print(' '.join(map(str, B)))
    
solve()