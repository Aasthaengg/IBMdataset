import collections

S = input()
T = input()

s = sorted(list(collections.Counter(S).values()))
t = sorted(list(collections.Counter(T).values()))

if s == t:
    print('Yes')
else:
    print('No')