def main():
    n = int(input())
    hs = list(map(int, input().split()))

    ans = 0
    while True:
        if sum(hs) == 0:
            break

        i = 0
        while (i < n):
            if hs[i] == 0:
                i += 1
            else:
                ans += 1
                while (i < n and hs[i] > 0):
                    hs[i] -= 1
                    i += 1
    print(ans)


if __name__ == "__main__":
    main()
