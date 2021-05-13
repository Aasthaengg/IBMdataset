def insertionSort(A,N):
    for i in range(0,N):
        v = A[i]
        j = i -1
        while j>=0 and A[j] > v :
            A[j+1] = A[j]
            j-=1
        A[j+1] = v
        print(*A, sep=" ")

N = int(input())
A = input().split()
A = list(map(int,A))
insertionSort(A,N)
