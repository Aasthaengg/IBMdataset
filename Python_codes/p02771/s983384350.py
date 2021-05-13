import sys
print('Yes' if len(frozenset(sys.stdin.readline().split())) == 2 else 'No')