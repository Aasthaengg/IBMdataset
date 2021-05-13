import collections
N = int(input())
S = [''.join(sorted(list(input()))) for i in range(N)]
c = collections.Counter(S)
print(sum([int(x * (x - 1) / 2) for x in c.values()]))