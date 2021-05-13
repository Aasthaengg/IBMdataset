def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    full = 0
    for i in range(N + 1):
        if i == 0:
            full += abs(A[0])
        elif i == N:
            full += abs(A[-1])
        else:
            full += abs(A[i] - A[i - 1])
    diff = [0 for _ in range(N)]
    for i in range(N):
        if i == 0:
            diff[0] = abs(A[1]) - (abs(A[1] - A[0]) + abs(A[0]))
        elif i == N - 1:
            diff[N - 1] = abs(A[-2]) - (abs(A[-2] - A[-1]) + abs(A[-1]))
        else:
            diff[i] = abs(A[i + 1] - A[i - 1]) - (abs(A[i + 1] - A[i]) + abs(A[i] - A[i - 1]))
    for d in diff:
        print(full + d)


if __name__ == '__main__':
    main()