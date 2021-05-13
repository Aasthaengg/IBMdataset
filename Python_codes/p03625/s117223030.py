N = int(input())
A = map(int, input().split())
import collections

A_count = collections.Counter(A)

keys = sorted(list(A_count.keys()), reverse=True)

hen_list = []
flag = 0
for key in keys:
    if A_count[key] >= 4:
        hen_list.append(key)
        hen_list.append(key)
    elif A_count[key] >= 2:
        hen_list.append(key)
    if len(hen_list) >= 2:
        flag = 1
        break
if flag == 1:
    print(hen_list[0] * hen_list[1])
else:
    print(0)