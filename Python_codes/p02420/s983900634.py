while True:
    s = str(input())
    if s == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)
