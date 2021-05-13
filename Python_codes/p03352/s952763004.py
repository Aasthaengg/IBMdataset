X = int(input())

max_num = 1
for i in range(1, X + 1):
    for j in range(2, X + 1):
        num = i ** j
        if num <= X:
            if num > max_num:
                max_num = num
        else:
            break

print(max_num)