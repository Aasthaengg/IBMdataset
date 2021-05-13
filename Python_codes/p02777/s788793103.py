def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    print(A - (U == S), B - (U == T))


if __name__ == '__main__':
    main()
