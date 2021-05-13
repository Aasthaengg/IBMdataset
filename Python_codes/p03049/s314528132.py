n = int(input())
s = [input() for _ in range(n)]

cnt_AB = 0
cnt_last_A = 0
cnt_start_B = 0
cnt_start_B_last_A = 0

for i in range(n):
    cnt_AB += s[i].count('AB')
    st = s[i][0]
    la = s[i][-1]
    if st == 'B' and la == 'A':
        cnt_start_B_last_A += 1
    elif st == 'B':
        cnt_start_B += 1
    elif la == 'A':
        cnt_last_A += 1

if cnt_start_B_last_A == 0:
    print(cnt_AB + min(cnt_start_B, cnt_last_A))
else:
    if cnt_start_B + cnt_last_A > 0:
        print(cnt_AB + cnt_start_B_last_A + min(cnt_start_B, cnt_last_A))
    else:
        print(cnt_AB + cnt_start_B_last_A - 1)
