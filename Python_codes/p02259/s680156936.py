def bubbleSort(A, N):
    c = 0
    flag = 1
    while flag:
        flag = 0
        for j in range(1, N):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                c += 1
                flag = 1
    print " ".join(map(str, A))
    print c


N = int(raw_input())
L = map(int, raw_input().split())

bubbleSort(L, N)