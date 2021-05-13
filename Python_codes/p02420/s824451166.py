while True:
    s = input()
    if s == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s += s[0:h]
        s = s[h:]
    print(s)
