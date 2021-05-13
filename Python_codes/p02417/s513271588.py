import string
from sys import stdin

chs = dict([(ch, 0) for ch in string.ascii_lowercase])

for line in stdin:
    for ch in line:
        c = ch.lower()

        if c not in chs:
            continue

        chs[c] += 1

for ch in string.ascii_lowercase:
    print(ch, ':', chs[ch])