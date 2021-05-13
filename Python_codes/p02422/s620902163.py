s = list(raw_input())
for loop in xrange(input()):
    c = raw_input().split()
    if c[0] == "replace":
        s[int(c[1]): int(c[2]) + 1] = list(c[3])
    if c[0] == "reverse":
        s[int(c[1]): int(c[2]) + 1] = s[int(c[1]): int(c[2]) + 1][::-1]
    if c[0] == "print":
        print "".join(s[int(c[1]): int(c[2]) + 1])