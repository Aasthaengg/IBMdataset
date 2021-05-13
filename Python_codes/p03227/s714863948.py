s = list(input())

if len(s)==2:
    print("".join(s))
else:
    print("".join(s[2]+s[1]+s[0]))