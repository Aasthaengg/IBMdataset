count_num = int(input())
a = map(int, input().split())
num_list = list(a)

num_list.sort(reverse=True)
max_num = num_list.pop(0)

sum_left_num = 0

for i in num_list:
    sum_left_num += i

if max_num < sum_left_num:
    print('Yes')
else:
    print('No')