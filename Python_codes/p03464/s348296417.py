import sys
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

K = ir()
A = lr()[::-1]
domain = [2, 2] #現在の最小と最大
for i in range(K):
    x = A[i]
    left = domain[0]; right = domain[1]
    if x > right * 2 - 1:
        print(-1)
        exit()
    left += (-left) % x
    right -= right % x
    right += x - 1
    if left > right:
        print(-1)
        exit()
    domain = [left, right]

print(*domain)
# 05