n = int(raw_input())
s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
h = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    x = raw_input().split()
    x[1] = int(x[1])
    if x[0] == "S":
        s[x[1]] = 1
    elif x[0] == "H":
        h[x[1]] = 1
    elif x[0] == "C":
        c[x[1]] = 1
    elif x[0] == "D":
        d[x[1]] = 1

for i in range(1,14):
    if s[i] != 1:
        print "S %d" %i
for i in range(1,14):
    if h[i] != 1:
        print "H %d" %i
for i in range(1,14):
    if c[i] != 1:
        print "C %d" %i
for i in range(1,14):
    if d[i] != 1:
        print "D %d" %i