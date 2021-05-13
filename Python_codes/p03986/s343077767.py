s = input()
n = len(s)
max_cnt = 0
cnt = 0
for i in range(n):
    if s[i] == 'T':
        cnt += 1
    else:
        cnt -= 1
    max_cnt = max(cnt, max_cnt)
print(2*max_cnt)