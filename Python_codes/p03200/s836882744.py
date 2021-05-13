s = input()
cnt = 0
b_cnt = 0
for c in s:
    if c == 'B':
        b_cnt += 1
    else:
        cnt += b_cnt
print(cnt)