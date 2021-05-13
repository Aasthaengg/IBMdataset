def main():
    n, x = map(int, input().split())
    m = [int(input()) for _ in range(n)]

    x -= sum(m)
    r = n + x // min(m)
    print(r)

if __name__ == '__main__':
    main()
