s = input()
n = len(s)
char_cnt = [s.count('a'), s.count('b'), s.count('c')]
char_cnt.sort(reverse=True)
if n % 3 == 0:
    suitable_cnt = [n//3, n//3, n//3]
elif n % 3 == 1:
    suitable_cnt = [n//3 + 1, n//3, n//3]
else:
    suitable_cnt = [n//3 + 1, n//3 + 1, n//3]

if char_cnt == suitable_cnt:
    print('YES')
else:
    print('NO')