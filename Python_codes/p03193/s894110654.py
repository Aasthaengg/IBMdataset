def main():
    n, h, w = list(map(int, input().split()))
    ans = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        if h <= a and w <= b:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
