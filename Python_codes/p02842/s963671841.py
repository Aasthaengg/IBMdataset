def resolve():
    paid = int(input())
    import math
    price = math.ceil(paid * 100 / 108)
    if price * 108 // 100 == paid:
        print(price)
    else:
        print(":(")


if __name__ == '__main__':
    resolve()