x = input()

ans = 0
s_cnt = 0

for i in range(len(x)):
    if s_cnt == 0:
        if x[i] == 'T':
            ans += 1
        else:
            s_cnt += 1
    else:
        if x[i] == 'T':
            s_cnt -= 1
        else:
            s_cnt += 1

if s_cnt > 0:
    ans += s_cnt

print(ans)
