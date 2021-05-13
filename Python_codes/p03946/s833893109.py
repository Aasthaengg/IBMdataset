n,t = map(int,input().split())
a = list(map(int,input().split()))

max1 = [0] * n
max1[-1] = a[-1]

for i in range(1, n):
    max1[-i-1] = max(max1[-i], a[-i-1])

ans = 0
tmp = -1

for i in range(n):
    if max1[i] - a[i] > tmp:
        tmp = max1[i] - a[i]
        ans = 1
    elif max1[i] - a[i] == tmp:
        ans += 1

print(ans)
