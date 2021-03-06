def main():
    N = int(input())
    ans = 0
    for x in range(1, int(N ** 0.5) + 1):
        # x(1+2+3+...+e)
        e = N // x
        ans += x * (e * e + e - x * x)
    print(ans)


if __name__ == '__main__':
    main()
