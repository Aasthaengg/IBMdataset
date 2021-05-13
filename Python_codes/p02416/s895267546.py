while True:
    X = input()
    if X == "0":
        break
    num = sum([int(x) for x in X])
    print(str(num))
