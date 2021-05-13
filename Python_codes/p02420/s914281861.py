from sys import stdin

while True:
    s = stdin.readline().rstrip()
    if s == "-":
        break
    else:
        m = int(stdin.readline().rstrip())
        for i in range(m):
            h = int(stdin.readline().rstrip())
            s = s[h:]+s[:h]
        else:
            print(s)
