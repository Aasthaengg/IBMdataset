import sys

alphabets = 'abcdefghijklmnopqrstuvwxyz'

cnt = {}
for c in alphabets:
    cnt[c] = 0

for line in sys.stdin:
    for c in line:
        if 'a' <= c.lower() <= 'z':
            cnt[c.lower()] += 1

for c in alphabets:
    print('%s : %d' % (c, cnt[c]) )