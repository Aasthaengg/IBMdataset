ar = list(input())
g = 0
p = 0
count = 0
for a in ar:
    if a == "g":
        if g == p:
            g += 1
        else:
            p += 1
            count += 1
    else:
        if g == p:
            g += 1
            count -= 1
        else:
            p += 1
print(count)