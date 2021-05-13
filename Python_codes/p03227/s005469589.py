s = str(input())
if len(s) == 2:
    print(s)
elif len(s) == 3:
    r = list(reversed(s))
    print(r[0]+r[1]+r[2])
