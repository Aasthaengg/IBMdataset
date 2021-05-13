def main():
    n, m, d = map(int, input().split())

    ans = 0
    if d == 0:
        ans = 1 / n
    else:
        ans = 2*(n-d)/(n*n)

    print(ans*(m-1))

if __name__ == '__main__':
    main()
