def main():
    X, A, B = [int(input()) for _ in range(3)]
    remain = X - A
    print(remain % B)

if __name__ == '__main__':
    main()