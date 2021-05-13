number = int(input())
cards = list(map(int, input().split()))


def insertionSort(A, N):
    print(" ".join(map(str, A)))
    for i in range(1, N):
        j = i - 1
        while A[j] > A[i] and j >= 0:
            A[i], A[j] = A[j], A[i]
            j -= 1
            i -= 1
        print(" ".join(map(str, A)))

insertionSort(cards, number)
