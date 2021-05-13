s = input()

a_cnt = 0
b_cnt = 0
c_cnt = 0
for i in range(len(s)):
    if s[i] == 'a':
        a_cnt += 1
    elif s[i] == 'b':
        b_cnt += 1
    else:
        c_cnt += 1
        
abc_max = max(a_cnt, b_cnt, c_cnt)
abc_min = min(a_cnt, b_cnt, c_cnt)

if abc_max < abc_min + 2:
    print('YES')
else:
    print('NO')