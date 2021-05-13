import sys
def input(): return sys.stdin.readline().strip()

mi = lambda: map(int, input().split())

a, b, c = mi()

print(max([0, c-(a-b)]))