S = input()
data_list = S.split()
ab_distance = abs(int(data_list[0])-int(data_list[1]))
ac_distance = abs(int(data_list[0])-int(data_list[2]))
bc_distance = abs(int(data_list[1])-int(data_list[2]))
d = int(data_list[3])
if ac_distance <= d:
    print('Yes')
elif ab_distance <= d and bc_distance <= d:
    print('Yes')
else:
    print('No')