while True:
    A = 0
    a = list(input())
    if a == ["0"]:
        break
    for x in a:
        A += int(x)
    print(A)

