def main():
    n_money, y_yen = map(int, input().split())
    # money
    a, b, c = 10000, 5000, 1000
    for x in range(n_money+1):
        for y in range(n_money-x+1):
            z = n_money - x - y
            money = a * x + b * y + c * z
            if money == y_yen:
                print(f'{x} {y} {z}')
                return 0
    print('-1 -1 -1')


if __name__ == '__main__':
    main()