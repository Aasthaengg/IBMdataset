import sys
from collections import Counter
S = list(input())
N = len(S)
S = Counter(S)
if len(S) == 1:
    if N == 1:
        print("YES")
        sys.exit()
    else:
        print("NO")
        sys.exit()
if len(S) == 2:
    if N == 2:
        print("YES")
        sys.exit()
    else:
        print("NO")
        sys.exit()

a = S["a"]
b = S["b"]
c = S["c"]
M = max(a, b, c)
m = min(a, b, c)

if (M-m) <= 1:
    print("YES")
else:
    print("NO")
