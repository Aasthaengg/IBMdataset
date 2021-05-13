s = input()
c, f = False, False
for i in s:
    if i == 'C':
        c = True
    elif c and i == 'F':
        f = True
print("Yes" if c and f else "No")
