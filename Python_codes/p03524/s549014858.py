s = input()
a_cnt = s.count('a')
b_cnt = s.count('b')
c_cnt = s.count('c')
if max(a_cnt, b_cnt, c_cnt) <= min(a_cnt, b_cnt, c_cnt) + 1:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)