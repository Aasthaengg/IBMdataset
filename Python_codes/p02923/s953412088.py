n = int(input())
h = list(map(int, input().split()))
nm = len(h)
ans = 0
for _ in range(nm):
    cnt = 0
    while True:
        if len(h) == 1:
            break
        if h[0] >= h[1]:
            cnt += 1
            h.pop(0)
        else:
            h.pop(0)
            break
    ans = max(ans, cnt)
print(ans)
