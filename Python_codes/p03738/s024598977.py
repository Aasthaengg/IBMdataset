import sys
def I(): return int(sys.stdin.readline().rstrip())

A,B = I(),I()
if A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')
