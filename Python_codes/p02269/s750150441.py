n = input()
S = set()
for i in xrange(n):
    inst, s = raw_input().split()
    if inst == "insert":
        S.add(s)
    else:
        if s in S:
            print "yes"
        else:
            print "no"