n = int(input())
a = list(map(int, input().split()))

cnt_1, cnt_2 = 0, 0
for v in a:
    if v % 2 == 1:
        cnt_1 += 1
    elif v % 4 == 0:
        cnt_2 += 1

if cnt_1 + cnt_2 == n and cnt_1 - cnt_2 == 1:
    print('Yes')
elif cnt_1 <= cnt_2:
    print('Yes')
else:
    print('No')