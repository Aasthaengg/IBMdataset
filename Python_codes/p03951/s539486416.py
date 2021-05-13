import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()
N = I()
s,t = S(),S()
ans = 2*N
for i in range(N,0,-1):
    if s[-i:]==t[:i]:
        ans -= i
        break
print(ans)
