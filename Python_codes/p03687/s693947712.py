s = input()
ans = len(s)
for i in range(26):
    c0 = chr(ord('a')+i)
    tmp = 0
    ma = 0
    for c in s:
        if c==c0:
            ma = max(ma, tmp)
            tmp = 0
        else:
            tmp += 1
    ma = max(ma, tmp)
    ans = min(ans, ma)
print(ans)