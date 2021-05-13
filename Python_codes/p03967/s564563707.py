S = input()
p_cnt = 0
for c in S:
    if c == 'p':
        p_cnt += 1
print(len(S)//2-p_cnt)