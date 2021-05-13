while True:
    s = raw_input()
    if s == "-":
        break

    for i in range(int(raw_input())):
        h = int(raw_input())
        s = s[h:] + s[0:h]

    print(s)