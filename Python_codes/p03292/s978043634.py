line = list(input().split())
line.sort()
if int(line[1]) - int(line[0]) > int(line[2]) - int(line[1]):
    print((int(line[2]) - int(line[1]) + (int(line[1]) - int(line[0]))))
else:
    print(abs((int(line[2]) - int(line[1]) + (int(line[1]) - int(line[0])))))