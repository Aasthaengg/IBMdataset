while 1:
    s = input()
    if s == '-':
        break
    m =int(input())
    for i in range(m):
        t = int(input())
        s = s[t:] + s[:t]
    print(s)

