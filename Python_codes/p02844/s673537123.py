N = int(input())
S = input()

num = "1234567890"

ans = 0
for a in num:
    pa = S.find(a)
    if pa == -1:
        continue
    for b in num:
        pb = S.find(b, pa + 1)
        if pb == -1:
            continue
        for c in num:
            pc = S.find(c, pb + 1)
            if pc == -1:
                continue
            ans += 1
print(ans)
