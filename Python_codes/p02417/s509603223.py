from sys import stdin
from string import ascii_lowercase

count_let = {k : 0 for k in ascii_lowercase}

s = list(stdin.read().rstrip().lower())
for c in s:
    count_let[c] = count_let.get(c, 0)+1

for k, v in sorted(count_let.items()):
    if k in ascii_lowercase:
        print("{} : {}".format(k, v))
