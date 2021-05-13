while True:
    s = input()
    if s == "-":
        break
    m = int(input())
    n = 0
    for i in range(m):
        n += int(input())
    n %= len(s)
    print(s[n:] + s[:n])