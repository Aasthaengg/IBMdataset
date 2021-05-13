from itertools import combinations
n,m = map(int,input().split())
ki = n*m
a = len(list(combinations(range(n+m),2)))
print(a-ki)