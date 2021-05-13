s = 'AKIHABARA'

import itertools

A = []
for i in range(1, len(list(s))+1):
    B = itertools.combinations(s, i)
    for j in B:
        string = "".join(j)
        if 'K' in string and 'I' in string and 'H' in string and 'B' in string and 'R' in string:
            A.append(string)
if input() in A:
    print("YES")
else:
    print("NO")