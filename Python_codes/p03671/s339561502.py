def main():
    bell_prices = sorted(list(map(int, input().split())))
    print(sum(bell_prices[:2]))


if __name__ == '__main__':
    main()

