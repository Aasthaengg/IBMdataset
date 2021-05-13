def main():
    n, k = map(int, input().split())
    print("YES" if 2 * (k - 1) + 1 <= n else "NO")


if __name__ == '__main__':
    main()

