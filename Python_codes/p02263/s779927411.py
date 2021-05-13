l = [i for i in input().split()]
s = []
for i in range(len(l)):
    if l[i] == "+":
        a = s.pop()
        b = s.pop()
        c = b + a
        s.append(c)
    elif l[i] == "-":
        a = s.pop()
        b = s.pop()
        c = b - a
        s.append(c)
    elif l[i] == "*":
        a = s.pop()
        b = s.pop()
        c = b * a
        s.append(c)
    else:
        s.append(int(l[i]))

print(s[0])