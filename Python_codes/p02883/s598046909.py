import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f = sorted(f, reverse=True)
cost = []
for i in range(n):
    cost.append(a[i]*f[i])
left = -1
right = max(cost)
def solve(x):
    cnt = 0
    for i in range(n):
        d = cost[i] - x
        if d <= 0:
            continue
        cnt += d//f[i] + int(d % f[i] != 0)
    if cnt <= k:
        return True
    else:
        return False
while right - left > 1:
    mid = (right + left) // 2
    if solve(mid):
        right = mid
    else:
        left = mid
print(right)