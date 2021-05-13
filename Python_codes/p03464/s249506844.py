import sys
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

K = ir()
A = lr()[::-1]
left = 2
right = 2
for x in A:
    left += (-left) % x
    right -= right % x
    right += x - 1

if left > right:
    print(-1)
else:
    print(left, right)
# 05
