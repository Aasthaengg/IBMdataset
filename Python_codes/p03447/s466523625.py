def main():
    money_on_hand = int(input())
    cake_cost = int(input())
    donut_cost = int(input())
    print((money_on_hand - cake_cost) % donut_cost)


if __name__ == '__main__':
    main()