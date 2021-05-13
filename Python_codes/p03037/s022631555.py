n, m = map(int, input().split())

left = 1
right = n+1

for i in range(m):
    l, r = map(int, input().split())
    left = max(left, l)
    right = min(right, r)

ans = right-left+1
print(ans if ans >= 0 else 0)