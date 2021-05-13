num_list = [int(x) for x in input().split()]
k = int(input())
print(sum(num_list) + max(num_list) * (2 ** k - 1))