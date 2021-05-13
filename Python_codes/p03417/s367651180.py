h, w = map(int, input().split())
h, w = min(h, w), max(h, w)
if h == 1:
    if w == 1:
        ans = 1
    elif w == 2:
        ans = 0
    else:
        ans = w - 2
elif h == 2:
    ans = 0
else:
    ans = (h - 2) * (w - 2)
print(ans)