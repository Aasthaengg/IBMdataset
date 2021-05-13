S = input()
i_list = list(S)
i_list = [int(i) for i in i_list]

if i_list[0] == i_list[1] or i_list[1] == i_list[2] or i_list[2] == i_list[3]:
    print('Bad')
else:
    print('Good')