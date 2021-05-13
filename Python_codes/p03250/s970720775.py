line = list(input().split())
line.sort()
line.reverse()
print(int(str(line[0]) + str(line[1])) + int(line[2]))