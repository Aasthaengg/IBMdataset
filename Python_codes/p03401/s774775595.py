import copy
def main():
    N = int(input())
    A = [0] + [int(a) for a in input().split()]

    total = 0
    for i in range(1, N + 1):
        if i != N:
            total += abs(A[i] - A[i - 1])
        else:
            total += abs(A[i] - A[i - 1])
            total += abs(A[i] - A[0])

    for i in range(1, N + 1):
        S = copy.deepcopy(total)

        if i != N:
            S -= (abs(A[i] - A[i-1]) + abs(A[i] - A[i + 1]))
            S += abs(A[i - 1] - A[i + 1])

        else:
            S -= (abs(A[i] - A[i - 1]) + abs(A[i] - 0))
            S += abs(A[i - 1] - 0)

        print(S)

if __name__ == "__main__":
    main()