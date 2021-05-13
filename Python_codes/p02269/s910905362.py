n = int(input())
l = set()

for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        l.add(cmd[1])
    if cmd[0] == 'find':
        if cmd[1] in l:
        	print('yes')
        else:
        	print('no')