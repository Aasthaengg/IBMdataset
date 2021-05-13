from collections import defaultdict

S = defaultdict(int)
for i in input():
    S[i] += 1

if len(S.values()) == 2:
    a, b = S.values()
    if a == b == 2:
        print('Yes')
        exit()
print('No')
