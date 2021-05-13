if __name__ == "__main__":
    n = int(raw_input())

    s = []
    h = []
    c = []
    d = []

    i = 0
    while i < n:
        v = raw_input().split()
        if v[0] == "S":
            s.append(int(v[1]))
        elif v[0] == "H":
            h.append(int(v[1]))
        elif v[0] == "C":
            c.append(int(v[1]))
        elif v[0] == "D":
            d.append(int(v[1]))
        i += 1

    i = 1
    while i <= 13:
       if i not in s:
           print "S {0}".format(i)
       i += 1

    i = 1
    while i <= 13:
       if i not in h:
           print "H {0}".format(i)
       i += 1

    i = 1
    while i <= 13:
       if i not in c:
           print "C {0}".format(i)
       i += 1

    i = 1
    while i <= 13:
       if i not in d:
           print "D {0}".format(i)
       i += 1