while True:
    t = input()
    if t == "-":
        break
    c = int(input())
    for i in range(c):
        h = int(input())
        t = t[h:] + t[:h]
    print(t)
