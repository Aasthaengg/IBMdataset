from sys import stdin
S = stdin.readline().rstrip()
flag = 0 
if 'AA' in S:
    flag = 1
if 'KA' in S:
    flag = 1
if 'IA' in S:
    flag = 1
if S.replace('A', '') != 'KIHBR':
    flag = 1
if flag:
    print('NO')
else:
    print('YES')