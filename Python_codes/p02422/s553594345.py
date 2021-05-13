st = input()
q = int(input())

for i in range(q):
    com = input().split()
    a = int(com[1])
    b = int(com[2])
    if com[0] == 'print':
        print(st[a:b + 1])
    elif com[0] == 'reverse':
        st = st[:a] + st[a:b + 1][::-1] + st[b + 1:]
    else:
        p = com[3]
        st = st[:a] + p + st[b + 1:]