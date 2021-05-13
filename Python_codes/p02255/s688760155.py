def insertionSort(A, N):
    for i in xrange(1, N):
        printList(A, N)
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j-=1
        A[j+1] = v
    return A

def printList(A, N):
    for i in xrange(N):
        print A[i],
    print

# MAIN
N = input()
A = map(int, raw_input().split())

A = insertionSort(A, N)
printList(A, N)