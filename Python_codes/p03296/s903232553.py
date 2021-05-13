from sys import stdin
from itertools import groupby
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
lin = []
for key, value in groupby(li):
    lin.append(len(list(value)))
print(sum(i//2 for i in lin))