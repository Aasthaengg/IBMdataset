def main():
    N = int(input())
    prices = [int(input()) for _ in range(N)]
    r = sum(prices) - max(prices) / 2
    print(int(r))

if __name__ == '__main__':
    main()
