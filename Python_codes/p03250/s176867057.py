num_list = list(map(int,input().split()))

num_list = sorted(num_list)

print(int(num_list[2]*10 + num_list[0] + num_list[1]))