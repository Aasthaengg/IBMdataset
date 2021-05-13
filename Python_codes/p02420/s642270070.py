while True:
    s = input()
    if s == "-":
        exit()
    else:
        m = int(input())
        sc = 0
        for i in range(m):
            sc += int(input())
        for i in range(sc):
            s = s[1:] + s[:1:]
        print(s)