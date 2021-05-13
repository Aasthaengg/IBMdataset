import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n, m = nm()
l, r = nm()
for i in range(m - 1):
    l_t, r_t = nm()
    l, r = max(l, l_t), min(r, r_t)
if r >= l:
    print(r - l + 1)
else:
    print(0)
