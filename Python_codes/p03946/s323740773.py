n, t = map(int,input().split())
a = list(map(int,input().split()))
amax = [a[-1]] * n

for i in range(n-2, -1, -1):
    amax[i] = max(amax[i+1], a[i])

cnt = 0
v = -10**10
for i in range(n-1):
    b = amax[i+1] - a[i]
    if b > v:
        v = b
        cnt = 1
    elif b == v:
        cnt += 1
print(cnt)