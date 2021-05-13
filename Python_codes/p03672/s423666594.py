s = input()
l = len(s)-2

while True:
    s = s[0:l]
    h = int(l/2)
    if s[0:h] == s[h:l]:
        print(l)
        exit(0)
    else:
        l = l-2
