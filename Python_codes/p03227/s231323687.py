s=input()

if len(s)==2:
    print(s)
else:
    for i in [2,1,0]:
        print(s[i], end="")
    print("")