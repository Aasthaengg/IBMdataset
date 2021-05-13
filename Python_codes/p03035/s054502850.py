import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B = LI()

if A <= 5:
    print(0)
elif A <= 12:
    print(B//2)
else:
    print(B)