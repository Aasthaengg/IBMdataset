import sys

def I(): return int(sys.stdin.readline().rstrip())

R = I()

if R < 1200:
    print('ABC')
elif R < 2800:
    print('ARC')
else:
    print('AGC')