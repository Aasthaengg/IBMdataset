def main():
    X, A, B = list(int(input()) for i in range(3))

    print((X - A) % B)

if __name__ == '__main__':
    main()