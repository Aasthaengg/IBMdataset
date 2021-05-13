# 131 B

n, l = map(int, input().split())
cmin = float('inf')
sum = 0

for i in range(1, n+1):
    f = l + i - 1
    sum += f
    if cmin >= 0:
        cmin = min(cmin, f)
    else:
        cmin = max(cmin, f)

print(sum - cmin)