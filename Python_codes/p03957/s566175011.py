s=input()
if s[:-1].count("C")>=1:
    x=s.index("C")
    if s[x:].count("F")>=1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    exit()