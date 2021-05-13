import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
ans = "second"
for n in range(N):
    if ir() % 2 == 1:
        ans = "first"
print(ans)
