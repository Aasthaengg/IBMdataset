def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())

    ans = n * x if k > n else k * x + (n - k) * y
    print(str(ans))
    return


if __name__ == '__main__':
    main()
