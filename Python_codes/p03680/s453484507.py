def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]

    tmp = 0

    for i in range(N):
        if a[tmp] == 2:
            print(i+1)
            exit()
        else:
            tmp = a[tmp]-1

    print(-1)


if __name__ == "__main__":
    main()
