in_str = raw_input()
q = int(raw_input())
for i in range(q):
    oper = raw_input().split()
    if oper[0] == 'print':
        print in_str[(int(oper[1])):(int(oper[2]))+1]
    elif oper[0] == 'reverse':
        buf = ''
        for i in range(int(oper[1])):
            buf += in_str[i]
        for i in reversed(range(int(oper[1]),int(oper[2])+1)):
            buf += in_str[i]
        buf += in_str[(int(oper[2]))+1:]
        in_str = buf
    elif oper[0] == 'replace':
        buf = in_str[:(int(oper[1]))]
        buf += oper[3]
        buf += in_str[(int(oper[2]))+1:]
        in_str = buf