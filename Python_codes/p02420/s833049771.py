result = []
while True:

    s = raw_input()
    if s == "-":
        break
    else:
        m = input()
        for i in xrange(m):
            h = input()
            s = s[h:len(s)] + s[0:h]
        
        result.append(s)

for i in result:
    print i 