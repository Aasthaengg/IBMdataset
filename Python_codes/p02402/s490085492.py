import sys

n = sys.stdin.readlines()

nstr = list(map(int, n[1].split(" ")))

print("{0} {1} {2}".format(min(nstr), max(nstr), sum(nstr)))