import collections
print(len(list(filter(lambda c: c % 2 == 1, list(collections.Counter([int(input()) for i in range(int(input()))]).values())))))
