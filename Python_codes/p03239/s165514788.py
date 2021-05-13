import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,T = MI()

ans = 10000
for i in range(N):
    c,t = MI()
    if t <= T:
        ans = min(ans,c)
print(ans if ans != 10000 else 'TLE')
