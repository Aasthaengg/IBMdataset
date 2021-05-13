def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    A, count = bubbleSort(A, N)

    print(' '.join([str(a) for a in A]))
    print(count)

def bubbleSort(A, N):
    flag = True
    count = 0

    while flag:
        flag = False

        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1
                flag = True

    return A, count

if __name__ == '__main__':
    main()