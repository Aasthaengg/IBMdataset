while True:
    x = input()
    if x == 0:
        break

    total = 0
    while x != 0:
        total += x % 10
        x = x//10

    print(total)