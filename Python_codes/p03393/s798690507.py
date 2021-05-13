import sys
from sys import stdin

s = stdin.readline().rstrip()
if len(s) == 26:
    count = 1
    for i in range(1, len(s)):
        if s[-i] < s[-i - 1]:
            count += 1
        else:
            break
    if count == 26:
        print(-1)
    else:
        for i in sorted(s[-count:]):
            if s[-count - 1] < i:
                print(s[:-count-1] + i)
                sys.exit()
else:
    d = {}
    for i in range(26):
        d.update({i: 0})
    for si in s:
        d[ord(si) - 97] += 1
    for i in range(26):
        if d[i] == 0:
            s += chr(i + 97)
            print(s)
            sys.exit()
