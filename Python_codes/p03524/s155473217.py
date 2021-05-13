import sys
input = sys.stdin.readline

s = input().rstrip()

from collections import Counter

c = Counter(s)

if len(s) == 1:
    print("YES")
    sys.exit()

if len(c.keys()) == 1:
    print("NO")
    sys.exit()

values = list(c.values())
values.sort()

if len(c.keys()) == 2:
    if values[0] == 1 and values[1] == 1:
        print("YES")
    else:
        print("NO")
    sys.exit()

values[1] -= values[0]
values[2] -= values[0]

if values[1] == 1 and values[2] == 1:
    print("YES")
elif values[1] == 0 and values[2] == 1:
    print("YES")
elif values[1] == 1 and values[2] == 0:
    print("YES")
elif values[1] == 0 and values[2] == 0:
    print("YES")
else: 
    print("NO")
sys.exit()

