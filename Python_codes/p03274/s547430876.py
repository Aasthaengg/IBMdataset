# https://atcoder.jp/contests/abc107/tasks/arc101_a

n, k = map(int, input().split())

nums = [int(i) for i in input().split()]

ans = float('inf')
for i in range(n - k + 1):
    l = nums[i]
    r = nums[i + k - 1]
    if l >= 0:
        t = r
    elif r <= 0:
        t = abs(l)
    else:
        t = min(abs(l), abs(r)) * 2 + max(abs(l), abs(r))
    ans = min(ans, t)

print(ans)