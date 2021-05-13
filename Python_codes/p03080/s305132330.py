from sys import stdin
N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
r = S.count('R')
b = S.count('B')
if r > b:
    print('Yes')
else:
    print('No')