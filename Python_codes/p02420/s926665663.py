while True:
    w = input()
    if '-' == w:
        break

    m = int(input())

    for i in range(m):
        h = int(input())
        w = w[h:]+w[0:h]

    print(w)