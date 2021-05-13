inp = [i for i in input().split()]
com = input()
for i in range(len(com)):
    if com[i] == "N":
        a = []
        a.append(inp[1])
        a.append(inp[5])
        a.append(inp[2])
        a.append(inp[3])
        a.append(inp[0])
        a.append(inp[4])
        inp = a
    elif com[i] == "S":
        a = []
        a.append(inp[4])
        a.append(inp[0])
        a.append(inp[2])
        a.append(inp[3])
        a.append(inp[5])
        a.append(inp[1])
        inp = a
    elif com[i] == "E":
        a = []
        a.append(inp[3])
        a.append(inp[1])
        a.append(inp[0])
        a.append(inp[5])
        a.append(inp[4])
        a.append(inp[2])
        inp = a
    elif com[i] == "W":
        a = []
        a.append(inp[2])
        a.append(inp[1])
        a.append(inp[5])
        a.append(inp[0])
        a.append(inp[4])
        a.append(inp[3])
        inp = a
print(inp[0])