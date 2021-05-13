import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

one = S()
two = S()

if one[0] == two[2] and one[1] == two[1] and one[2] == two[0]:
    print('YES')
else:
    print('NO')