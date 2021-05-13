def main():
    n, i = map(int, input().split())
    train = list(range(1, n+1))[::-1]
    ans = train.index(i) + 1
    print(ans)


if __name__ == "__main__":
    main()
