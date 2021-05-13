def selectionSort(A, N): 
    m = 0
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j] < A[minj]:
                minj = j
        A[i],A[minj] = A[minj],A[i]
        if i != minj:
            m += 1
    print ' '.join(map(str,A))
    print m

N = int(raw_input())
A = map(int,raw_input().split())
selectionSort(A,N)