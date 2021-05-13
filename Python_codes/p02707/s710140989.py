N = int(input())
A_list = [int(i) for i in input().split()]

staff_count_list = [0] * N

for i in A_list:
    staff_count_list[i - 1] += 1
for i in staff_count_list:
    print(i)