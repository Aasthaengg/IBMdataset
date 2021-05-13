s = list(str(input()))
t = list(str(input()))

s.append(t[-1])

if s == t:
    print('Yes')
else:
    print('No')