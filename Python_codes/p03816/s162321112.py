import collections
n = int(raw_input())
ais = map(int, raw_input().split())
cc = collections.Counter(ais)
k = n - len(cc)
print len(cc) - (1 if (n - len(cc)) % 2 == 1 else 0)
