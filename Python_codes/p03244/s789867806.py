from collections import Counter

n = int(input())
L = list(map(int, input().split()))
L1 = L[::2]
L2 = L[1::2]
c1 = Counter(L1).most_common()
c2 = Counter(L2).most_common()
if len(set(L1)) == len(set(L2)) == 1:
    if c1[0] == c2[0]:
        print(len(L1))
    else:
        print(0)
else:
    if c1[0] != c2[0]:
        print(n - c1[0][1] - c2[0][1])
    else:
        print(min(n - c1[0][1] - c2[1][1], n - c1[1][1] - c2[0][1]))
