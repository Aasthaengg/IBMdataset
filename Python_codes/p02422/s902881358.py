str, q = input(), int(input())
for i in range(q):
    com = input().strip().split()
    if com[0] == 'print':
        print(str[int(com[1]):int(com[2])+1])
    elif com[0] == 'reverse':
        str = list(str)
        str[int(com[1]):int(com[2])+1] = str[int(com[2]):int(com[1])-len(str)-1:-1]
        str = ''.join(str)
    elif com[0] == 'replace':
        str = list(str)
        str[int(com[1]):int(com[2])+1] = com[3]
        str = ''.join(str)