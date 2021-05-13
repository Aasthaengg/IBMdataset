import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
print('ABC' if N <= 999 else 'ABD')
