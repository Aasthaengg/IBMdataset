while True:
    s = input()
    if s == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        tmp = s[:h]
        s = s[h:]
        s += tmp
    print(s)