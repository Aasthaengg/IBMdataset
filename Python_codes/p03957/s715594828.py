s = input()
if s.count("C")>=1 and s.count("F")>=1:
    if s.index("C")<s.index("F") or s.index("C")<len(s)-(1+s[::-1].index("F")):
        print("Yes")
    else:
        print("No")
else:
    print("No")