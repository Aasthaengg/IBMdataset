n, m = map(int,input().split())
a = list(map(int, input().split()))
t = 0

for i in range(m):
    t += a[i]
    if t > n:
        break
if t > n:
    ans = -1
else:
    ans = n - t

print(ans)