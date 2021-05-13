import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


L = LI2()
N = len(L)
mod = 10**9+7

ans = 0
a = 1

for i in range(N):
    if L[i] == 1:
        ans += pow(3,N-i-1,mod)*a
        ans %= mod
        a *= 2
        a %= mod

print((ans+a) % mod)
