import sys
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし


L = LI2()
N = len(L)
mod = 10**9+7

a = 1
b = 0

for i in range(N):
    if L[i] == 1:
        b += pow(3,N-i-1,mod)*a
        b %= mod
        a *= 2
        a %= mod

print((a+b) % mod)
