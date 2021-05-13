while True:
    s = input()
    if s == "-":
        break
    l = list(s)
    m = int(input())
    top = 0
    for i in range(m):
        h = int(input())
        top = (top+h) % len(l)
    for i in range(top, top+len(l)):
        print(l[i%len(l)],end="")
    print("")