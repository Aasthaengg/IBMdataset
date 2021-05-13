from sys import stdin
from itertools import combinations_with_replacement

n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))

ave = sum(li)/n
mi = 10**9
now = 0
for i,j in enumerate(li):
    if abs(j-ave) < mi:
        mi = abs(j-ave)
        now = i
print(now)