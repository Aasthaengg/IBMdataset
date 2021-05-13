instr = raw_input().strip()
commandnum = input()
for c in xrange(commandnum):
    command = raw_input().split()
    if command[0]=="replace":
        instr = instr[:int(command[1])]+command[3]+instr[int(command[2])+1:]
    elif command[0]=="reverse":
        instr = instr[:int(command[1])]+instr[int(command[1]):int(command[2])+1][::-1]+instr[int(command[2])+1:]
    elif command[0]=="print":
        print instr[int(command[1]):int(command[2])+1]
    else:
        print "invalid command."
        break