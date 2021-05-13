x = list(input())
n = len(x)
ct = 0
cs = 0
c = 0
for X in x:
    if X == "S":
        cs += 1
    else:
        ct += 1
        if cs >= 1:
            cs -= 1
            c += 1
print(n-2*c)