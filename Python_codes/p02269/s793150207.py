import sys
input()
d = {}
for s in sys.stdin:
    if s[0]=='i':
        d[s[7:]] = 1
    else:
        if s[5:] in d:
            print('yes')
        else:
            print('no')
