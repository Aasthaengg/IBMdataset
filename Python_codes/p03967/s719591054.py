a = input()
g = 0
p = 0
s = 0
for i in range(len(a)):
    if a[i] == "g":
        g += 1
    else:
        p += 1
c = abs((g-p)//2)
if g < p:
    g += c
    p -= c
elif g > p:
    p += c
    g -= c
d = "p" * p + "g" * g
for i in range(len(a)):
    if a[i] != d[i]:
        if a[i] == "p" and d[i] == "g":
            s -= 1
        elif a[i] == "g" and d[i] == "p":
            s += 1
print(s)
