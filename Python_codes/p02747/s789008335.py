import sys

s = input()

while len(s) > 0:
    if len(s) == 1:
        print('No')
        sys.exit()
    else:
        if s[:2] == 'hi':
            s = s[2:]
        else:
            print('No')
            sys.exit()

print('Yes')