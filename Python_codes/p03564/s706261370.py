import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
K = I()

ans = 1
for i in range(N):
    ans = min(ans*2,ans+K)
print(ans)