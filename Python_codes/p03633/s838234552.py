import sys

def I(): return int(sys.stdin.readline().rstrip())

N = I()
T = [I() for _ in range(N)]

from fractions import gcd

ans = T[0]
for i in range(N-1):
    ans = (ans*T[i+1])//gcd(ans,T[i+1])

print(ans)