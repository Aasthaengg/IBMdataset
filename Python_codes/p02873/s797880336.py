def sigma(x):
    a = 0
    for i in range(x):
        a += i + 1
    return a

s = input()
ans = 0
prev = ''
cnt = 0
p_cnt = 0
for i in s:
    if i == prev:
        cnt += 1
    else:
        if i =='<':
            ans += sigma(cnt - 1) + max(cnt, p_cnt)
        else:
            ans += sigma(cnt - 1)
        prev = i
        p_cnt = cnt
        cnt = 1
else:
    if prev == '<':
        ans += sigma(cnt)
    else:
        ans += sigma(cnt - 1) + max(cnt, p_cnt)
print(ans)