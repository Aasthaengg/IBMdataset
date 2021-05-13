s = input()

c = s.find("C")
f = s.find("F", c)

if c != -1 and f != -1:
    print("Yes")
else:
    print("No")
