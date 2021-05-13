nxt = ""
pre = ""
ans = 0
for c in input():
    nxt += c
    if nxt != pre:
        ans += 1
        pre = nxt
        nxt = ""

print(ans)
