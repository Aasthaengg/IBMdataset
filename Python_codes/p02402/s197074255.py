n = input()
data_list = list(input("").split())
min_array = min(map(int,data_list))
max_array = max(map(int,data_list))
sum_array = sum(map(int,data_list))
print("{0} {1} {2}".format(min_array, max_array, sum_array))