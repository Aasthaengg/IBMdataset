def main():
    n, m = map(int, input().split())
    ans = [-1] * n

    for i in range(m):
        s, c = map(int, input().split())

        if ans[s - 1] != -1:
            if ans[s - 1] != c:
                print(-1)
                exit()

        if n != 1 and s == 1 and c == 0:
            print(-1)
            exit()

        ans[s - 1] = c

    for i in range(n):
        if ans[i] == -1:
            if n == 1:
                ans[i] = 0
            else:
                if i == 0:
                    ans[i] = 1
                else:
                    ans[i] = 0

    print(*ans, sep="")


if __name__ == "__main__":
    main()
