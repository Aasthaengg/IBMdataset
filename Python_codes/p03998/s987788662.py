s = [input() for i in range(3)]
dex = 0
next = 'a'
while True:
    if next == 'a': dex = 0
    elif next == 'b': dex = 1
    else: dex = 2
    if s[dex] == "":
        print(next.upper())
        exit()
    next = s[dex][0]
    s[dex] = s[dex][1:]