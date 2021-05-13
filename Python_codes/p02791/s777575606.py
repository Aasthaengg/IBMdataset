N = int(input())
P_list = [int(_) for _ in input().split()]

count = 0
min_value_dic = {}
min_value_so_far =1e6
for i in range(N):
    if P_list[i] < min_value_so_far:
        min_value_dic[i] = P_list[i]
        min_value_so_far = P_list[i]
    else:
        min_value_dic[i] = min_value_so_far

# print(min_value_dic)

for i in range(N):
    if P_list[i] <= min_value_dic[i]:
        count +=1

print(count)