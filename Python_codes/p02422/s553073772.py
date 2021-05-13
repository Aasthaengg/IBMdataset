instr = input()
cnum = int(input())
for i in range(cnum):
    lineSp = input().split()
    cmd = lineSp[0]
    a, b = int(lineSp[1]), int(lineSp[2])
    if cmd == "replace":
        repstr = lineSp[3]
        instr = instr[0:a] + repstr + instr[b + 1:]
    elif cmd == "reverse":
        repstr = instr[a:b + 1][::-1]
        instr = instr[0:a] + repstr + instr[b + 1:]
    else:
        print(instr[a:b + 1])

