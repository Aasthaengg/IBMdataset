s = input()

cnt = 0
for i in s:
    if (i == 'o'):
        cnt += 1
print('YES' if len(s) - cnt <= 7 else 'NO')
