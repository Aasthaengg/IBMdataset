import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


L,R = MI()
if L//2019 != R//2019:
    print(0)
else:
    A = [i for i in range(L % 2019,(R % 2019)+ 1)]
    N = len(A)
    ans = 2019
    for i in range(N-1):
        for j in range(i+1,N):
            ans = min(ans,(A[i]*A[j]) % 2019)
    print(ans)
