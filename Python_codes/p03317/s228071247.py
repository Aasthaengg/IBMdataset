input_line = input().split()

num_array = int(input_line[0])
num_equal = int(input_line[1])

input_line = input() # 無視

equalized = 1
i = 0
while equalized < num_array:
    equalized += (num_equal - 1)
    # print(i, equalized)
    i += 1

print(str(i))
