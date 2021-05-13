s = input()

anum = 0
while s[anum] != "A":
    anum += 1
znum = len(s)-1
while s[znum] !="Z":
    znum -= 1

print(znum - anum +1)