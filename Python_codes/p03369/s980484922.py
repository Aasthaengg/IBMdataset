def resolve():
    s = input().strip()
    price = 700
    for i in range(3):
        if s[i] == 'o':
            price = price + 100
    print(price)
resolve()
