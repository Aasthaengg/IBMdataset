import collections

N,*A = map(int, open(0).read().split())
B = collections.Counter(A)
print(len([v for k,v in B.items() if v % 2]))