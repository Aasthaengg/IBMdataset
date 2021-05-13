from collections import Counter
S = input()
a = Counter(S)


if len(a) == 2 and len(set(list(a.values()))) == 1:
    print('Yes')
else:
    print('No')


