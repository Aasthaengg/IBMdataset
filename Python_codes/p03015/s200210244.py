import sys

def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

L = LI2()
l = len(L)
mod = 10**9+7

A = []
for i in range(l):
    if L[i] == 1:
        A.append(l-i-1)
A.append(0)

ans = 0
for i in range(len(A)):
    ans += pow(3,A[i],mod)*pow(2,i,mod)
    ans %= mod

print(ans)