n = int(input())
h = list(map(int, input().split()))

maxi = 0
now = h[0]
cnt = 0
for i in range(1, n):
    if h[i] <= now:
        cnt += 1
        now = h[i]
        maxi = max(maxi, cnt)
    else:
        cnt = 0
        now = h[i]
print(maxi)