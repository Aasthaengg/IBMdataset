N = int(input())
s = input()

r_cnt = 0
b_cnt = 0
for i in range(N):
    if s[i] == 'R':
        r_cnt += 1
    else:
        b_cnt += 1
if r_cnt > b_cnt:
    print('Yes')
else:
    print('No')
