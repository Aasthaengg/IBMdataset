def main():
    N = int(input())
    A = (int(x) - 1 for x in input().split())
    print(sum(A))


if __name__ == '__main__':
    main()
