line = list(input().split())
line.sort()
if line[0] != line[2]:
    if line[0] == line[1] or line[1] == line[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")