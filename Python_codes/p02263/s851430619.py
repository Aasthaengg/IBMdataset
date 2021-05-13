x = raw_input().split()
s = []
for e in x:
    try:
        s.append(int(e))
    except:
        b = s.pop()
        a = s.pop()
        if e == '+':
            s.append(a+b)
        if e == '-':
            s.append(a-b)
        if e == '*':
            s.append(a*b)
print s.pop()