def selectionSort(A, N):
    cnum = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            cnum += 1
    print " ".join(str(t) for t in A)
    print cnum

if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    selectionSort(A, N)