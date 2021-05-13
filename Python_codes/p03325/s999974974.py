import sys

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))


n = ri()
li = rl()
ans = 0
for i in li:
    t = 0
    while i & 1 == 0:
        i //= 2
        t += 1
    ans += t
print(ans)

