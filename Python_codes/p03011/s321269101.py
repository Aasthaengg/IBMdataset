import sys
import itertools
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A = LI()

A = list(itertools.combinations(A,2))
jikans = []
for a in A:
    a[0] + a[1]
    jikans.append(a[0] + a[1])

jikans.sort()
print(jikans[0])