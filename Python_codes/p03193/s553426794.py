n, h, w = map(int, input().split())
ab=[map(int,input().split()) for _ in range(n)]
a, b = [list(_) for _ in zip(*ab)]
ans=0
for i in range(n):
    if a[i] >= h and b[i] >= w:
        ans += 1
print(ans)