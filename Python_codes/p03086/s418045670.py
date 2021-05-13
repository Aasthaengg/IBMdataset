s = list(input())
cnt, new_cnt = 0, 0
for x in s:
    if x == "A" or x == "C" or x == "G" or x == "T":
        new_cnt += 1
        if cnt < new_cnt:
            cnt = new_cnt
    else:
        new_cnt = 0

print(cnt)
