while True:
    n = raw_input()
    if n=="0":
        break
    ans = 0
    for x in xrange(len(n)):
        ans += int(n[x])
    print ans