Str = input()
atgc = ['A', 'T', 'G', 'C']
max_cnt = 0
cnt = 0
for s in Str:
    if s in atgc:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 0
print(max_cnt)
