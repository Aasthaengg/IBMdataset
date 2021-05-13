a = int(input())
b = list(input())
d = list(b[0])
if a < len(b):
    for c in range(a-1):
        d.append(b[c+1])
    d.append("...")
    d = "".join(d)
    print(d)
else:
    b = "".join(b)
    print(b)