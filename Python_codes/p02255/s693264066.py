def solve():
    N = int(input())
    A = [int(i) for i in input().split()]

    InsertionSort(N, A)

def InsertionSort(N, A):
    print(*A)
    for i in range(1, N):
        v = A[i]
        for j in range(i - 1, -1, -1):
            if A[j] > v:
                A[j + 1] = A[j]
            else:
                A[j + 1] = v
                break
        else:
            A[0] = v

        print(*A)

if __name__ == '__main__':
    solve()