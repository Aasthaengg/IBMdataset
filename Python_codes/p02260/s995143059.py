def selection_sort(A, N):
    c = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
 
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            c += 1
    print " ".join(map(str, A))
    print c


n = int(raw_input())
A = map(int, raw_input().split())

selection_sort(A, n)