N,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = 0
for i in range(N):
    x -= a[i]
    if x < 0:
        break
    res += 1
if x > 0:
    res -= 1
print(res)