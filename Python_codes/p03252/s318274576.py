from collections import Counter
S = input()
T = input()
c_S = Counter(S)
c_T = Counter(T)
# print('c_S, c_T', c_S, c_T)
v1 = sorted(c_S.values())
v2 = sorted(c_T.values())
if len(v1) != len(v2):
    print('No')
    exit()
for s1, s2 in zip(v1, v2):
    if s1 != s2:
        print('No')
        exit()
print('Yes')
