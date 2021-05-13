s = input()
i = 0
l = list()
for c in s:
    if (i%2 == 0):
        l.append(c)
    i = i+1
l = "".join(l)
print(l)
