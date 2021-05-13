n = int(input())
num_list = [int(i) for i in input().split()]
count = 0

for i in range(1,n):
    if num_list[i] < num_list[i-1]:
        count += (num_list[i-1] - num_list[i])
        num_list[i] = num_list[i-1]

print(count)