nums = int(input())
total = 0

for num in range(1, nums+1):
    len_num = len(str(num))
    if len_num % 2 == 1:
        total += 1

print(total)