from itertools import*
n, k = map(int, input().split())
print(min(sum(len(list(l))-1 for _, l in groupby(input())) + 2*k, n-1))