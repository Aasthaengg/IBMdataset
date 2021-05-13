
def print_array(A, N):
    for i in xrange(N - 1):
        print str(A[i]),

    print A[N - 1]

def selectionSort(A, N):
    swap_num = 0
    for i in xrange(0, N):
        minj = i
        for j in xrange(i, N):
            if A[j] < A[minj]:
                minj = j

        if minj != i:
            swap_num += 1
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp

    return swap_num

def main():
    N = int(raw_input())
    A = []

    for num in raw_input().split():
        A.append(int(num))

    temp = selectionSort(A, N)
    print_array(A, N)

    print temp


if __name__ == "__main__":
    main()