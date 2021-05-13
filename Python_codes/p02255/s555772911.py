def show_list(num_list):
    for i in range(len(num_list)):
        print(str(num_list[i]), end="")
        if i < len(num_list)-1:
            print(" ", end="")
        else:
            print()

input_num = int(input())
num_list = [int(i) for i in input().split()]
show_list(num_list)
for i in range(1, len(num_list)):
    v = num_list[i]
    j = i - 1
    while j >= 0 and num_list[j] > v:
        num_list[j+1] = num_list[j]
        j -= 1
    num_list[j+1] = v
    show_list(num_list)