from collections import Counter
import math
h, w = map(int, input().split())
data = ''
for _ in range(h):
    a = input()
    data += a
cnt = Counter(data)
data_list = list(cnt.values())
cnt_list = []
for hh in range(math.ceil(h / 2)):
    for ww in range(math.ceil(w / 2)):
        if (hh == math.floor(h / 2)) & (ww == math.floor(w / 2)):
            cnt_list.append(1)
        elif (hh == math.floor(h / 2)) | (ww == math.floor(w / 2)):
            cnt_list.append(2)
        else:
            cnt_list.append(4)
cnt_count = Counter(cnt_list)
ans = 'Yes'

cnt_4 = 0
while cnt_4 < cnt_count[4]:
    for c in range(len(data_list)):
        if ((data_list[c]) >= 4) & (data_list[c] > 0):
            data_list[c] -= 4
            cnt_4 += 1
        if cnt_4 == cnt_count[4]:
            break
    if cnt_4 == cnt_count[4]:
        ans = 'Yes'
        break
    if len([d for d in data_list if d >= 4]) == 0:
        ans = 'No'
        break

cnt_2 = 0
while cnt_2 < cnt_count[2]:
    for c in range(len(data_list)):
        if ((data_list[c] >= 2) & (data_list[c] > 0)):
            data_list[c] -= 2
            cnt_2 += 1
        if cnt_2 == cnt_count[2]:
            break
    if cnt_2 == cnt_count[2]:
        ans = 'Yes'
        break
    if len([d for d in data_list if d >= 2]) == 0:
        ans = 'No'
        break
    
cnt_1 = 0
while cnt_1 < cnt_count[1]:
    for c in range(len(data_list)):
        if (data_list[c] > 0):
            data_list[c] -= 1
            cnt_1 += 1
        if cnt_1 == cnt_count[1]:
            break
    if cnt_1 == cnt_count[1]:
        ans = 'Yes'
        break
    if len([d for d in data_list if d >= 1]) == 0:
        ans = 'No'
        break

if (sum(data_list) == 0) & (ans != 'No'):
    print('Yes')
else:
    print('No')