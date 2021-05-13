def main():
    X, Y = map(int, input().split())
    ans = 1
    for _ in range(Y + 1):
        if 2 * X <= Y:
            X *= 2
            ans += 1
        else:
            print(ans)
            quit()


if __name__ == "__main__":
    main()
