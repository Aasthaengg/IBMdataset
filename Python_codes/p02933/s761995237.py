import sys

def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

a = I()
s = S()

if a >= 3200:
    print(s)
else:
    print('red')