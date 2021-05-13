import sys

s = [x.strip() for x in sys.stdin.readlines()]
for i, j in enumerate(s):
    if j == '0':
        break
    print('Case {}: {}'.format(i + 1, j))