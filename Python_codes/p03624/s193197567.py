from sys import stdin

s = stdin.readline().strip()
a = set('abcdefghijklmnopqrstuvwxyz')
b = a - set(s)

if len(b) == 0: print('None')
else: print(min(b))