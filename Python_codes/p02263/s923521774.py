s = []
e = input().split()

for c in e:
    if c in "+-*":
        a = s.pop()
        b = s.pop()
        s.append(str(eval(b + c + a)))
    else:
        s.append(c)

print(s[0])

