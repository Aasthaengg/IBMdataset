def main():
    X, Y, Z = map(int, input().split())
    X, Y = Y, X
    X, Z = Z, X

    print(X, Y, Z)


if __name__ == '__main__':
    main()