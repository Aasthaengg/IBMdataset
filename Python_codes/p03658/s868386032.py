def main():
    n, k = map(int, input().split())
    L = list(map(int, input().split()))

    print(sum(sorted(L)[::-1][:k]))

if __name__ == '__main__':
    main()