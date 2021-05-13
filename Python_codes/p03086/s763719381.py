s = str(input())

cnt = 0
max_cnt = 0
acgt = ["A", "C", "G", "T"]

for e in s:
    if(acgt.count(e) == 1):
        cnt += 1
    else:
        if(cnt >= max_cnt):
            max_cnt = cnt
        cnt = 0

if(cnt >= max_cnt):
    max_cnt = cnt
print(max_cnt)
