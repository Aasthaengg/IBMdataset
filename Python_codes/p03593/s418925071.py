h,w = map(int,input().split())

d = {}
for _ in range(h):
    a = input()
    for i in range(w):
        a1 = a[i]
        if a1 in d:
            d[a1] += 1
        else:
            d[a1] = 1

if h % 2 == 0 and w % 2 == 0:
    for v in d.values():
        if v % 4 != 0:
            print('No')
            exit()
    print('Yes')

elif h % 2 == 0 or w % 2 == 0:
    cnt_4 = (h // 2) * (w // 2)
    if h % 2 == 0:
        cnt_2 = h // 2
    else:
        cnt_2 = w // 2
    tmp_2 = 0
    tmp_4 = 0
    for v in d.values():
        if v % 4 == 0:
            tmp_4 += v // 4
        elif v % 2 == 0:
            tmp_4 += v // 4
            tmp_2 += 1
        else:
            print('No')
            exit()
    if tmp_4 >= cnt_4 and cnt_2 == tmp_2 + (tmp_4 - cnt_4) * 2:
        print('Yes')
    else:
        print('No')

else:
    cnt_4 = (h // 2) * (w // 2)
    cnt_2 = h // 2 + w // 2
    cnt_1 = 1
    tmp_1 = 0
    tmp_2 = 0
    tmp_4 = 0

    for v in d.values():
        if v % 4 == 0:
            tmp_4 += v // 4
        elif v % 2 == 0:
            tmp_4 += v // 4
            tmp_2 += 1
        else:
            tmp_4 += v // 4
            tmp_2 += (v % 4) // 2
            tmp_1 += 1
    if tmp_4 >= cnt_4 and cnt_2 <= tmp_2 + (tmp_4 - cnt_4) * 2 and cnt_1 == tmp_1 + tmp_2 + (tmp_4 - cnt_4) * 2 - cnt_2:
        print('Yes')
    else:
        print('No')
