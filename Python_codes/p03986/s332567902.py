X = list(str(input()))
n = len(X)

s = []
for x in X:
    if x == 'S':
        s.append(x)
    if x == 'T':
        if s:
            if s[-1] == 'S':
                s.pop()
            else:
                s.append(x)
        else:
            s.append(x)
print(len(s))
