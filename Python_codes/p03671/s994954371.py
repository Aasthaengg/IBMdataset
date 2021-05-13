from sys import stdin
from itertools import accumulate

li = list(map(int,stdin.readline().rstrip().split()))

li.sort()

print(li[0]+li[1])