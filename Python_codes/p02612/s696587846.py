def calc_change(price: int) -> int:
    while price >= 1000:
        price = price - 1000
    return 1000 - price if not price == 0 else 0

if __name__=='__main__':
    print(calc_change(int(input())))