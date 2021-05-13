num_num = int(input())
numbers = list(map(int, input().split()))
numbers_even = []

for i in range(num_num):
    if numbers[i] % 2 == 0:
        numbers_even.append(numbers[i])
    else:
        pass
i = 1
for even in numbers_even:
    if even % 3 == 0 or even % 5 == 0:
        i += 1
        if i == num_num:
            break
    else:
        print("DENIED")
        exit()

print("APPROVED")
