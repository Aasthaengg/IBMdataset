import os, sys, math
if os.environ.get("DEBUG") is not None:
    sys.stdin = open("in.txt", "r")
rl = sys.stdin.readline

n = int(rl())
a = list(map(int, rl().split()))

ans = math.inf
for it in a:
    cnt = 0
    while it > 0 and it % 2 == 0:
        it /= 2
        cnt += 1
    ans = min(ans, cnt)
print(ans)
