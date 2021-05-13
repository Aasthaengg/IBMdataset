import itertools
for i in itertools.count(1):
    n = int(input())
    if n==0:
        break
    print('Case {}: {}'.format(i, n))