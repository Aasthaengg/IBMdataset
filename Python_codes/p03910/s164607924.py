n = int(input())

sum = 0
num_list = []
for i in range(1, 10**7):
    sum += i
    num_list.append(i)
    if sum > n:
        break

for i in num_list:
    if i == (sum - n):
        continue
    else:
        print(i)