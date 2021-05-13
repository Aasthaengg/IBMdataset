def main():
    n = int(input())
    ans = 0
    minr = int(input())
    ans = -1 * 10**9
    for i in range(n-1):
        r = int(input())
        ans = max(ans, r-minr)
        minr = min(minr, r)

    print(ans)


if __name__ == '__main__':
    main()
