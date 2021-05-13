def main():
    A, B, C = map(int, input().split())
    price = [A, B, C]
    price.sort()
    print(price[0] + price[1])
main()