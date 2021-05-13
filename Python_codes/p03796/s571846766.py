import sys
def I(): return int(sys.stdin.readline().rstrip())
N = I()
ans = 1
for i in range(1,N+1):
    ans *= i
    ans %= 10**9+7
print(ans)
