n = int(raw_input())
L = []
c = 0
for i in xrange(n):
    cmd = raw_input()
    if cmd[0] == "i":
        L.append(cmd[7:])
    elif cmd[6] == " ":
        try:
            L.pop(~L[::-1].index(cmd[7:]))
        except:
            pass
    elif cmd[6] == "F":
        L.pop()
    else:
        c += 1

print " ".join(map(str, L[c:][::-1]))