s = input()
s_cnt =0
t_cnt =0
cnt = 0

for i in range(len(s)):
    if s[i] == 'S':
        s_cnt += 1
    if s[i] == 'T':
        t_cnt += 1
        if s_cnt >0:
            t_cnt -= 1
            s_cnt -= 1
print(t_cnt + s_cnt)
