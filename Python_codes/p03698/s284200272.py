def resolve():
    S = input()
    c = set()
    l = 0
    for s in S:
        c.add(s)
        if l == len(c):
            print("no")
            return
        l += 1
    print("yes")


resolve()
