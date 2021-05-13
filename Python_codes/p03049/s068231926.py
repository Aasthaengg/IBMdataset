import re

n = int(input())
w = x = y = z = 0
for i in range(n):
    s = input()
    t = re.sub(r'AB', "X", s)
    w += len(s) - len(t)
    if s[0] == "B":
        if s[-1] == "A":
            x += 1
        else:
            y += 1
    elif s[-1] == "A":
        z += 1
if x > 1:
    w += x - 1
    x = 1
if max(x, y, z) == y:
    w += x
    w += z
elif max(x, y, z) == z:
    w += x
    w += y
print(w)