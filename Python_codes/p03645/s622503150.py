n, m = map(int, input().split())
ans = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        ans[b - 1] += 1
    elif b == n:
        ans[a - 1] += 1

if 2 in ans:
    print("POSSIBLE")
else:
     print("IMPOSSIBLE")