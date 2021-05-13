A = list(reversed(input()))
B = list(reversed(input()))
C = list(reversed(input()))

d = {'a': A, 'b': B, 'c': C}
cur = 'a'

import sys

while True:
    if len(d[cur]) == 0:
        print(cur.upper())
        sys.exit()
    
    cur = d[cur].pop()
