N = input()
i_list = list(N)
i_list = [int(i) for i in i_list]

if i_list[0] == i_list[1] and i_list[1] == i_list[2]:
    print('Yes')
elif i_list[1] == i_list[2] and i_list[2] == i_list[3]:
    print('Yes')
else:
    print('No')