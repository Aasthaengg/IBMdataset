def SelectionSort(A):
    count = 0
    for i in range(len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    print(" ".join(map(str, A)))
    print(count)


n = int(input())
A = list(map(int, input().split()))

SelectionSort(A)