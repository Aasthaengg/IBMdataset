def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    for i in range(n):
        if a[i] % 2 == 1:
            print("first")
            exit()
    print("second")

if __name__ == '__main__':
    main()
