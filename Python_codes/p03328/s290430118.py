import itertools

n, m = map(int, input().split())
l = list(itertools.accumulate(range(1, 1000)))
print(l[m-n-1]-m)