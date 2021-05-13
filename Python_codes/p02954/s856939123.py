s = input().rstrip() + 'X'

r_cnt = l_cnt = 0
is_r = True
begin_l = None
ans = [0] * (len(s)-1)
for i in range(len(s)):
    if is_r and s[i] == 'R':
#         print(f'{i}: R')
        r_cnt += 1
    elif not is_r and s[i] == 'L':
#         print(f'{i}: L')
        l_cnt += 1
    elif s[i] == 'L':
#         print(f'{i}: R>L')
        is_r = False
        l_cnt = 1
        begin_l = i
    else:
#         print(f'{i}: L>?')
        is_r = True
#         print(l_cnt, r_cnt)
        tot = l_cnt + r_cnt
        small = tot//2
        large = tot - small
        if r_cnt%2:
            ans[begin_l-1] = large 
            ans[begin_l] = small
        else:
            ans[begin_l-1] = small
            ans[begin_l] = large
        r_cnt = 1
        l_cnt = 0

print(*ans)