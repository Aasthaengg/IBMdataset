#%%

n, h, w = map(int, input().split())
a = [0] * n
b = [0] * n
ans = 0

for i in range(n):
    a[i], b[i] = map(int, input().split())
    if a[i] >= h and b[i] >= w:
        ans += 1

print(ans)