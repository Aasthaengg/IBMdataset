import sys
import string

count = {k : 0 for k in string.ascii_lowercase}
for c in sys.stdin.read().lower():
    if c.islower():
        count[c] = count[c] + 1
for k, v in count.items():
    print(f"{k} : {v}")
