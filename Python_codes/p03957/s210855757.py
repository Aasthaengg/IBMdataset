s = input()
t = s.find("C")
if s[t:].find("F") > 0:
    print("Yes")
else:
    print("No")