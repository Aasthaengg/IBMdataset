s = input()
stack, p = 0, 0
for i in s:
    if i == "S":
        stack += 1
    elif stack > 0 and i == "T":
        p += 1
        stack -= 1
    else:
        pass
print(len(s) - p * 2)
