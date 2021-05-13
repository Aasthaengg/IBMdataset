# A - Two Abbreviations
from fractions import gcd

N,M = map(int,input().split())
S = input()
T = input()

GCD = gcd(len(S),len(T))
LCM = len(S) * len(T) // GCD
ans = LCM

for i in range(GCD):
    if S[i*len(S)//GCD]!=T[i*len(T)//GCD]:
        ans = -1
        break

print(ans)