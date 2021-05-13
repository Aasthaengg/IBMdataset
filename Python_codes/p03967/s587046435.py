S = input()

g = 0
p = 0
w = 0
l = 0
for s in S:
    if g <= p:
        t = "g"
    else:
        t = "p"

    if t == "p" and s == "g":
        w += 1
    elif t == "g" and s == "p":
        l += 1
    if t == "g":
        g += 1
    else:
        p += 1

print(w-l)