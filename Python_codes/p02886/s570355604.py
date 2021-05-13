import itertools
n = int(input())

d = list(map(int,input().split()))
ans = 0

a = list(itertools.combinations(d, 2))

print(sum(i*j for i, j in a))
