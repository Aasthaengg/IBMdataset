N = int(input())
A_list = []
A_list.append(list(map(int, input().split())))
A_list.append(list(map(int, input().split())))


candy_max_count = 0
for switch_path_index in range(N):
    candy_count = sum(A_list[0][0:switch_path_index + 1]) + sum(A_list[1][switch_path_index:N])
    candy_max_count = max(candy_max_count, candy_count)

print(candy_max_count)