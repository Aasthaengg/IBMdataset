import sys

def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

N = I()
S,T = S().split()
S = list(S)
T = list(T)

ans = ''
for i in range(N):
    ans += S[i]+T[i]

print(ans)