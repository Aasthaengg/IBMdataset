N = int(input())
a_list = list(map(int,input().split()))

cnt = 0
tmp_cnt = 0
tmp_a = 0
for a in a_list:
    if a == tmp_a:
        tmp_cnt += 1
        if tmp_cnt % 2 == 0:
            cnt += 1
    else:
        tmp_a = a
        tmp_cnt = 1
        
print(cnt)