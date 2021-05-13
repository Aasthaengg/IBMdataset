import sys
def I(): return int(sys.stdin.readline().rstrip())

x = I()
print('ABC' if x < 1200 else 'ARC')
