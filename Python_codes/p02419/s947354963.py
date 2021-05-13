import sys
W = input().casefold()
print(sum(line.casefold().split().count(W) for line in sys.stdin.readlines()))