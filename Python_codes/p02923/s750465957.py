n = int(input())
h = list(map(int, input().split()))

ans = 0
cnt = 0
prev = h[0]
for hi in h[1:]:
    if hi <= prev:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    prev = hi
print(max(ans, cnt))
