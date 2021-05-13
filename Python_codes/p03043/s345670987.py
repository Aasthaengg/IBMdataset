import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,K = MI()
ans = 0
if N >= K:
    ans += (N-K+1)/N
for i in range(1,min(K-1,N)+1):
    a = i
    r = 0
    while a <= K-1:
        a *= 2
        r += 1
    ans += 1/(N*2**r)

print(ans)
