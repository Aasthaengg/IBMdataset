def bubbleSort(A, N):
    cnum = 0
    flag = True
    while flag:
        flag = False
        for j in range(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp
                cnum += 1
                flag = True
    print " ".join([str(t) for t in A])
    print cnum

if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    bubbleSort(A, N)