s = input()
count_a = s.count('a')
count_b = s.count('b')
count_c = s.count('c')
if abs(count_a - count_b) <= 1 and abs(count_b - count_c) <= 1 and abs(count_c - count_a) <= 1:
    print('YES')
else:
    print('NO')