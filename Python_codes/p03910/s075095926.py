n = int(input())

num_sum = 0
max_num = 1
for i in range(n+1):
    num_sum += i
    if num_sum >= n:
        max_num = i
        break

for i in range(1, max_num+1):
    if i != num_sum - n:
        print(i)
