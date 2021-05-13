def main():
    A, B = map(int, input().split())
    print(A * B if 1 <= A <= 9 and 1 <= B <= 9 else -1)


if __name__ == '__main__':
    main()
