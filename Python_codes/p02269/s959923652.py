import sys
n = int(input())
d = {}
for op in sys.stdin.readlines():
    op = op.split()
    if op[0] == 'insert':
        d[op[1]] = 1  
    elif op[0] == 'find':
        if op[1] in d:
            print('yes')
        else:
            print('no')