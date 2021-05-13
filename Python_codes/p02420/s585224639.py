import sys
while True:
    s = input()
    if s == '-':
        sys.exit()
    m = int(input())
    for _ in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)
