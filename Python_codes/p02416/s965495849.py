while True:
    data = int(input())
    if data == 0:
        break

    sum = 0
    while data > 0:
        sum += data % 10
        data //= 10
    print(sum)