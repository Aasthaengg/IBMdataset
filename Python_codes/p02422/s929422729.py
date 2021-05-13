str = input()
q = int(input())

for i in range(q):
    com = input().split()
    a = int(com[1])
    b = int(com[2])
    if com[0] == 'print':
        print(str[a:b+1])
    elif com[0] == 'reverse':
        str = str[0:a] + str[a:b+1][::-1] + str[b+1:]
    elif com[0] == 'replace':
        str = str[0:a] + com[3] + str[b+1:]