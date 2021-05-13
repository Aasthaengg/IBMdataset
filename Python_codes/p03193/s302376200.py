nhw_list = list(map(int, input().split()))
tup_list = []
for i in range(nhw_list[0]):
    tup_list.append(list(map(int, input().split())))
count = 0
for tuple in tup_list:
    if tuple[0] >= nhw_list[1] and tuple[1] >= nhw_list[2]:
        count += 1
print(count)