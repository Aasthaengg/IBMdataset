import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
if N == 1:
    print('Hello World')
else:
    print(I()+I())
