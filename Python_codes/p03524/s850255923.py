s = input()

a_cnt = s.count('a')
b_cnt = s.count('b')
c_cnt = s.count('c')

if abs(a_cnt - b_cnt) <= 1 and abs(a_cnt - c_cnt) <= 1 and abs(b_cnt - c_cnt) <= 1:
    print('YES')

else:
    print('NO')