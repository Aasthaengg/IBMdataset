S = list(open(0).read())
ss = []
for s in S:
    if 'a' <= s <= 'z':
        ss.append(s.upper())
    elif 'A' <= s <= 'Z':
        ss.append(s.lower())
    else:
        ss.append(s)
print("".join(ss), end="")
