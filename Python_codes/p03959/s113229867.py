import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mt = [1]*n
Mt = [None]*n
ma = [1]*n
Ma = [None]*n
v = -1
for i,h in enumerate(t):
    if h>v:
        mt[i] = Mt[i] = h
    else:
        Mt[i] = h
    v = h
v = -1
for i,h in enumerate(reversed(a)):
    if h>v:
        ma[n-1-i] = Ma[n-1-i] = h
    else:
        Ma[n-1-i] = h
    v = h
ans = 1
M = 10**9+7
for i in range(n):
    val = min(Mt[i], Ma[i]) - max(mt[i], ma[i]) + 1
    if val<=0:
        ans = 0
        break
    ans *= val
    ans %= M
print(ans)