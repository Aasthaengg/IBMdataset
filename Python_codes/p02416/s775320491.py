while True:
    s = raw_input()
    if s == "0":
        break
    sum = 0
    for i in xrange(len(s)):
        sum += int(s[i:i+1])

    print sum