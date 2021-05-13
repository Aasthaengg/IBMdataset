import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,M = MI()
ab = [tuple(MI()) for _ in range(N)]
cd = [tuple(MI()) for _ in range(M)]

for i in range(N):
    a,b = ab[i]
    min_dis = 10**10
    k = 100
    for j in range(M):
        c,d = cd[j]
        if min_dis > abs(a-c) + abs(b-d):
            k = j+1
            min_dis = abs(a-c) + abs(b-d)
    print(k)

