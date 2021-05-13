import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,c,k = list(map(int, input().split()))
ts = [None]*n
for i in range(n):
    ts[i] = int(input())
ts.sort()
ans = 0
last = -float("inf")
num = 0
for t in ts:
    if last<t or num==c:
        last = t+k
        num = 1
        ans += 1
    else:
        num += 1
print(ans)