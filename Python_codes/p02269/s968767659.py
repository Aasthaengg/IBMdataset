from sys import stdin

n = int(stdin.readline())

d = {}
for i in range(n):
    cmd = stdin.readline()
    if cmd.startswith('insert'):
        s = cmd[7:-1]
        d[s] = True
    elif cmd.startswith('find'):
        s = cmd[5:-1]
        print('yes' if s in d else 'no')
