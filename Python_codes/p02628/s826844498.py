def main():
    n, k = map(int, input().split())
    fruits = list(map(int, input().split()))

    print(sum(sorted(fruits)[:k]))


if __name__ == '__main__':
    main()
