def main():
    D, N = (int(i) for i in input().split())
    if N == 100:
        N += 1
    print(N*100**D)


if __name__ == '__main__':
    main()
