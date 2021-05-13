S = input()
w_position_list = []
for i, s in enumerate(S):
    if s == 'W':
        w_position_list.append(i)
n_w = len(w_position_list)
res = sum(w_position_list) - (n_w *(n_w-1)/2)
print(int(res))