s = list(input())

ans = len(s)
for t in s:
    m = 0
    cnt = 0
    # 同じ文字の区間の最大値がその文字の最小値
    for S in s:
        if S == t: 
            m = max(m,cnt)
            cnt = 0
        else:
            cnt += 1
    m = max(m,cnt)
    ans = min(ans,m)
print(ans)