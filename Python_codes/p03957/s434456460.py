s = input()

iC = s.find('C')
if iC < 0:
    print("No")
    exit()

iF = s[iC:].find("F")
if iF < 0:
    print("No")
    exit()

print("Yes")