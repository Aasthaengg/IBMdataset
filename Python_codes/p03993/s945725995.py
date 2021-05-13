def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    ans = 0
    pair = [False for i in range(N)]

    for i in range(N):
        if (A[A[i] - 1] - 1 == i) and (pair[A[i] - 1] == False):
            ans += 1
            pair[i] = True
            pair[A[i] - 1] = True

    print(ans)

if __name__ == "__main__":
    main()