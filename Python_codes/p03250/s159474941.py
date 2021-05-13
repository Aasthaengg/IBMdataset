A, B, C = map(int, input().split())
num_list = [A, B, C]
num_list.sort()
print(num_list[2]*10+num_list[1]+num_list[0])
