def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0

    for cnt in range(2, N + 2):
        D += L[cnt - 2]
        if D > X:
            cnt -= 1
            break

    print(cnt)


if __name__ == "__main__":
    main()
