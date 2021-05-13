n = int(input())
number_list = []
for i in range(1, n + 1):
    if i % 15 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        number_list.append(i)

print(sum(number_list))