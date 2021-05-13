import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()
N = I()
s,t = S(),S()
ans = 2*N
minus = 0
for i in range(1,N+1):
    if s[-i:]==t[:i]:
        minus = max(minus,i)
print(ans-minus)
