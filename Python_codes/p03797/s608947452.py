def main():
    n, m = map(int, input().split())
    ans = 0
    if m >= 2*n:
        ans += n
        m -= 2*n
        n = 0
    else:
        ans += m // 2
        m -= ans * 2
    ans += m // 4
    print(ans)


if __name__ == "__main__":
    main()
