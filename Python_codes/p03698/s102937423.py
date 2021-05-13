import collections
c = collections.Counter(input()[:])

if c.most_common()[0][1] == 1:
    print('yes')
else:
    print('no')
