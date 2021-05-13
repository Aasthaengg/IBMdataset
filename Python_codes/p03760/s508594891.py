o = input()
e = input()
s = ""
for a in range(max(len(o), len(e))):
    try:
        s += o[a]
    except IndexError:
        pass
    try:
        s += e[a]
    except IndexError:
        pass
print(s)