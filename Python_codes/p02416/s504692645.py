while True:
    a = input()
    if a == "0":
        break
    else:
        b = list(a)
        c = [int(b[i]) for i in range(len(b))]
        print(sum(c))    