
N = int(input())

a_str = input()
a_list = [int(j) for j in a_str.split(' ')]

average = sum(a_list)/len(a_list)

fark_min = abs(a_list[0] - average)
save_list = []
for i in range(len(a_list)):
    fark = abs(a_list[i]-average)
    if fark <= fark_min:
        fark_min = fark

for i in range(len(a_list)):
    fark = abs(a_list[i] - average)
    if fark == fark_min:
        save_list.append(i)

print(min(save_list))

