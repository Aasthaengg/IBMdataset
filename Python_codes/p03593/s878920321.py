h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
 
cnt = {}
for ai in a:
    for c in ai:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
c1 = 0
c2 = 0
c4 = 0
for k, v in cnt.items():
    c4 += (v // 4) * 4
    c2 += ((v % 4) // 2) * 2
    c1 += v % 2
 
ans = "No"
if h % 2 == 0:
    if w % 2 == 0:
        if c4 == h * w:
            ans = "Yes"
    else:
        if c2 <= h and c1 == 0:
            ans = "Yes"
else:
    if w % 2 == 0:
        if c2 <= w and c1 == 0:
            ans = "Yes"
    else:
        if c2 <= h + w - 1 and c1 == 1:
            ans = "Yes"
print(ans)