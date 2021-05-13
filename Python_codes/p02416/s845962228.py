while True:
    x = input()
    if x=='0':
        break
    print(sum([int(x[i]) for i in range(len(x))]))