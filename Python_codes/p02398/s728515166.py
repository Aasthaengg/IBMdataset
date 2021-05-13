my_value = input()
my_value_list = ([int(x) for x in my_value.split()])

count = 0
for i in range(my_value_list[0], my_value_list[1]+1):
    if my_value_list[2] % i == 0:
        count += 1

print(count)