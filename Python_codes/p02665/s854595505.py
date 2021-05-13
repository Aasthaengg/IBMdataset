def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 0:
        if A[0] == 1:
            print(1)
        else:
            print(-1)
        exit()

    bound = [0] * (N+1)
    bound[0] = 1
    flag = True

    for i in range(1, N+1):
        bound[i] = (bound[i-1] - A[i-1]) * 2
        if bound[i] < A[i]:
            flag = False

    if not flag:
        print(-1)
        exit()

    B = [0] * (N+2)
    for i in range(N, -1, -1):
        tmp = min(bound[i], B[i+1] + A[i])
        B[i] = tmp

    print(sum(B))


if __name__ == "__main__":
    main()
