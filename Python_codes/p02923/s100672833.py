n = int(input())
hl = list(map(int, input().split()))

ans = 0
cnt = 0
prev_h = 0
for h in hl:
    if h > prev_h:
        ans = max(ans,cnt)
        cnt = 0
    else:
        cnt += 1
    prev_h = h

ans = max(ans,cnt)
print(ans)