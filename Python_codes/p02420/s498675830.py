while True:
    w = list(input())
    if w == ["-"]:
        break
    m = int(input())
    h = []
    for x in range(m):
        y = int(input())
        w = w[y:] + w[:y]
    for x in w:
        print(x, end = "")
    print()

