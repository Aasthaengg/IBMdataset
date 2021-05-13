s = input()

if len(s) == 3:
    l = s[:]
    s = l[2] + l[1] + l[0]

print(s)