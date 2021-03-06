import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
a = LI()

s,t = 0,0
for i in range(N):
    if a[i] % 4 == 0:
        s += 1
    elif a[i] % 2 == 0:
        t += 1

if s >= N//2 or t >= N-2*s:
    print('Yes')
else:
    print('No')