N = int(input())
a = list(map(int,input().split()))
if len(set(a)) == 1 and a[0] == 0:
    print("Yes")
    exit()
if N%3 != 0:
    print("No")
    exit()

import collections
sa = list(set(a))
sa.sort()
B = collections.Counter(a)

if len(sa) == 2 and 0 in sa:
    if B[0] == N//3 and B[sa[1]] == N*2//3:
        print("Yes")
    else: print("No")
    exit()
if len(sa) != 3:
    print("No")
    exit()

if B[sa[0]] == B[sa[1]] == B[sa[2]]:
    print("Yes" if sa[0] ^ sa[1] == sa[2] else "No")
else:
    print("No")