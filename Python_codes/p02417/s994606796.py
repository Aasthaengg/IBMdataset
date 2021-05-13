import string
c = {}
while True:
    try:
        for x in raw_input().lower():
            if not x.isalpha():
                continue
            c[x] = c.get(x, 0) + 1
    except EOFError, e:
        break

for x in string.ascii_lowercase:
    print("%s : %d" % (x, c.get(x, 0)))