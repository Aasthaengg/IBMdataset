n = int(input())
input_list = []

for i in range(n):
    input_list.append(int(input()))

sorted_list = sorted(input_list)

unique_list = set(sorted_list)

print(unique_list.__len__())