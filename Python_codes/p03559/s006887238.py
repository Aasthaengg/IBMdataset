import sys
from bisect import bisect_left,bisect_right


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
A,B,C = LI(),LI(),LI()
A.sort()
C.sort()

print(sum(bisect_left(A,b)*(N-bisect_right(C,b)) for b in B))
