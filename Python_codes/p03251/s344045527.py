n, m, x, y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
ans = 'War'
for z in range(max(xs) + 1, min(ys) + 1):
    if x < z <= y:
        ans = 'No War'
        break
print(ans)