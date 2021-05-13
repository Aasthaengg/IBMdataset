s = input()
c = s.find("C")
if c == -1:
    print("No")
    exit()
f = s.find("F", c+1)
if f == -1:
    print("No")
    exit()
print("Yes")