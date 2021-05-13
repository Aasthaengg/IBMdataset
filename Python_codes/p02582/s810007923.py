n = input()
r = 0
Tr = 0
for i in n:
    if i == "R":
        r += 1
        Tr = r
    elif i == "S":
        r = 0
print(Tr)
