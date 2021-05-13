s = input()
cnt = 0
if s[1] == 'S':
    if 'R' in s:
        cnt += 1
else:
    cnt += 1
    if s[0] == 'R':
        cnt += 1
    if s[2] == 'R':
        cnt += 1
print(cnt)
