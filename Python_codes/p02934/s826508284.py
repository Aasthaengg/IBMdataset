def main():
    N = input()
    A = map(int, input().split())
    v = sum([1 / a for a in A])
    print(1 / v)


if __name__ == '__main__':
    main()
