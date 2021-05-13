line = list(input())
line.sort()
if line[0] == line[1] and line[2] == line[3] and line[1] != line[2]:
    print("Yes")
else:
    print("No")