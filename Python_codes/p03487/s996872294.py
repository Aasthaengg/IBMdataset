import collections
n,cc = raw_input(), collections.Counter(map(int, raw_input().split()))
print sum([(cc[k] - k if k <= cc[k] else cc[k]) for k in cc] or [0])