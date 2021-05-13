cmd = []
d = set()

n = int(input())
for i in range(n):
    cmd.clear()
    cmd = input().split()
    if cmd[0] =='insert':
        d.add(cmd[1])
    else:
        if cmd[1] in d:
            print('yes')
        else:
            print('no')
