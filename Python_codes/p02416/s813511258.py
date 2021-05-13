while True:
    x = input()
    if x == "0":
        break
    sum_x = 0
    for X in x:
        sum_x += int(X)
    print(sum_x)