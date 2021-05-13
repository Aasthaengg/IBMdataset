def main():
    D, N = map(int, input().split())

    if N < 100:
        print(100**D*N)
    else:
        print(100**D*101)


if __name__ == "__main__":
    main()
