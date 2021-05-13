import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
guide = []
for i in range(N):
    s,p=LS()
    guide.append([s,100-int(p),i+1])
guide.sort()
for a in guide:
    print(a[2])