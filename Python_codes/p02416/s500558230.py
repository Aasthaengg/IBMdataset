while True:
    a = input()
    if a == "0":
        break
    a = [int(i) for i in a]
    print(sum(a))