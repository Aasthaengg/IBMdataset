num_list = [int(i) for i in input().split()]
K = int(input())

max_sum = max(num_list)*2**K + sum(num_list) - max(num_list)

print(max_sum)