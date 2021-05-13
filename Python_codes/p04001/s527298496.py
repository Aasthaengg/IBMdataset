S = input()

res_list = []

for i in range(2**(len(S)-1)):
    temp_s = ''
    for j in range(len(S)):
        temp_s += S[j]
        if ((i >> j) & 1):
            temp_s += '+'
    # print(temp_s)
    res_list.append(temp_s)

temp_S_list = [eval(item) for item in res_list]

print(sum(temp_S_list))