LI = lambda: list(map(int, input().split()))

N = int(input())
A = [int(input()) for _ in range(N)]


def main():
    a = 1
    for i in range(N + 1):
        if a == 2:
            print(i)
            return 0
        a = A[a - 1]
    print(-1)


if __name__ == "__main__":
    main()
