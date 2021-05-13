# coding: UTF-8
num_list = []
while(1):
    num = [map(int,raw_input())]
    if num[0][0] == 0:
        break
    num_list.extend(num)
for i in range(len(num_list)):
    print sum(num_list[i])
