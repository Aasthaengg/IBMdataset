import sys
from collections import Counter

S = sys.stdin.readline().strip()
counter = Counter(S)

ls = len(S)
if ls == 1:
    print("YES")
elif ls == 2:
    if len(counter) == 2:
        print("YES")
    else:
        print("NO")
else:
    if len(counter) < 3:
        print("NO")
    else:
        counter = sorted(counter.items(), key=lambda x: x[1])
        if counter[2][1] - counter[0][1] < 2:
            print("YES")
        else:
            print("NO")