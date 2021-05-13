import sys


k = 'abcdefghijklmnopqrstuvwxyz'
alp = {}

for i in k:
    alp[i] = 0


s = input()

for i in s:
    if alp[i] == 0:
        alp[i] = 1
    else:
        print('no')
        sys.exit()

print('yes')
