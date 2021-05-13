def main():
    N = int(input())
    A = [0]
    A += list(map(int, input().split()))
    A.append(0)
    total_dist = sum([abs(A[i+1] - A[i]) for i in range(N + 1)])
    for i in range(1, N + 1):
        print(total_dist - abs(A[i+1] - A[i]) - abs(A[i] - A[i-1]) + abs(A[i+1] - A[i-1]))


if __name__ == '__main__':
    main()
