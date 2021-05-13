n = int(input())
ns = list(map(int, input().split()))
sum_i = 0
cnt = 0
for i in range(n):
    sum_i += ns[i]
    if i % 2 == 0:
        if sum_i > 0:
            continue
        elif sum_i < 0:
            cnt += abs(sum_i) + 1
            sum_i = 1
        else:
            cnt += 1
            sum_i = 1
    else:
        if sum_i > 0:
            cnt += sum_i + 1
            sum_i = -1
        elif sum_i < 0:
            continue
        else:
            cnt += 1
            sum_i = -1
min_cnt = cnt
cnt = 0
sum_i = 0
for i in range(n):
    sum_i += ns[i]
    if (i+1) % 2 == 0:
        if sum_i > 0:
            continue
        elif sum_i < 0:
            cnt += abs(sum_i) + 1
            sum_i = 1
        else:
            cnt += 1
            sum_i = 1
    else:
        if sum_i > 0:
            cnt += sum_i + 1
            sum_i = -1
        elif sum_i < 0:
            continue
        else:
            cnt += 1
            sum_i = -1
print(min(min_cnt, cnt))