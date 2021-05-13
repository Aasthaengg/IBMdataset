s = input()
l = set(s)
ans = 10**10
for x in l:
    tmp, chk = 0, 0
    for i in s:
        if i != x:
            tmp += 1
        else:
            chk = max(chk, tmp)
            tmp = 0
    chk = max(chk, tmp)
    ans = min(chk, ans)
print(ans)