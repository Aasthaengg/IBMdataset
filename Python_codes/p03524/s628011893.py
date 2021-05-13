import sys
from collections import Counter

S = sys.stdin.readline().strip()
counter = Counter(S)
counter = sorted(counter.items(), key=lambda x: x[1])
# print(counter)

if len(counter) == 1:
    if counter[0][1] == 1:
        print("YES")
    else:
        print("NO")
elif len(counter) == 2:
    if counter[0][1] == 1 and counter[1][1] == 1:
        print("YES")
    else:
        print("NO")
else:
    if counter[0][1] + 1 < counter[2][1]:
        print("NO")
    else:
        print("YES")