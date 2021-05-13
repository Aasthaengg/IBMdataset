S = input()

calc_list = []
for i in range(len(S)-2):
    calc_list.append(abs(753-int(S[i:i+3])))

print(min(calc_list))