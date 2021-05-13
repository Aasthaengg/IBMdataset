# encode: utf-8

def selectionSort(A, N):
    count = 0
    for i in xrange(0, N):
        minj = i
        for j in xrange(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i] , A[minj] = A[minj], A[i]
            count += 1
    return A, count

def main():
    n = input()
    a = map(int, raw_input().split())
    a, count = selectionSort(a, n)
    print " ".join(map(str, a))
    print count

main()