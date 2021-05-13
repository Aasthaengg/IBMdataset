import fileinput

for line in fileinput.input():
    tokens = list(map(int, line.strip().split()))
    a, b = tokens[0], tokens[1]
    d = a * b
    if a < b:
        tmp = a
        a = b
        b = tmp

    c = a % b
    while(c != 0):
        a = b
        b = c
        c = a % b

    g = b
    l = d / g

    print(str(g)+" "+str(int(l)))