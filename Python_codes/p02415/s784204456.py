import sys
import math

S = raw_input()

for x in S:
    if "a" <= x <= "z":
        sys.stdout.write(x.upper())
    elif "A" <= x <= "Z":
        sys.stdout.write(x.lower())
    else:
        sys.stdout.write(x)
print