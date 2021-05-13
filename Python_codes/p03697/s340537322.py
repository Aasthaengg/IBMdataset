def main():
    N, M = (int(i) for i in input().split())
    print(N + M if N + M <= 9 else "error")


if __name__ == '__main__':
    main()
