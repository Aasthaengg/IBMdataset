def main():

    N, K = map(int, input().split())
    if (N+1) // 2 >= K:
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())