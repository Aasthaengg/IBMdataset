n = int(input())
h = list(map(int, input().split()))

ans = 0
prev = h[0]
c = 0
for i in range(1, n):
    if prev >= h[i]:
        c += 1
    else:
        c = 0
    prev = h[i]
    ans = max(ans, c)
print(ans)