S = input().strip()
z = 0
o = 0
r = 0
for s in S:
    if s == "0":
        if o > 0:
            o -= 1
            r += 2
        else:
            z += 1
    elif s == "1":
        if z > 0:
            z -= 1
            r += 2
        else:
            o += 1
print(r)
