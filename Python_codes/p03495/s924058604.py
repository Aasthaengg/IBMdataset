import collections
n, k = map(int, raw_input().split())
cvs = collections.Counter(map(int , raw_input().split())).values()
cvs.sort(key = lambda x:- x)
print sum(cvs[k:] or [0])