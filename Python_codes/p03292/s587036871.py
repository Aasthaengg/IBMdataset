A_1, A_2, A_3 = (int(x) for x in input().split())
list = [A_1, A_2, A_3]
new_list = sorted(list)
print(new_list[2] - new_list[0])