while True:
    d = raw_input()
    s = 0
    if int(d) == 0:
        break
    for c in d:
        v = ord(c) - ord('0')
        s = s + v
    print s