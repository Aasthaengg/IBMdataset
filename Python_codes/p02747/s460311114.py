import sys

s = input()
for _ in range(5):
    if len(s) == 1:
        print('No')
        sys.exit()
    if len(s) == 0:
        print('Yes')
        sys.exit()
    if s[:2] == 'hi':
        s = s[2:]
    else:
        print('No')
        sys.exit()
print('Yes')
