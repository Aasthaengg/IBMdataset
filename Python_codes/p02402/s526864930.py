num = int(input())
inps = input().split()
num_list = [int(i) for i in inps]
smallest = num_list[0]
largest = num_list[0]
total = 0
for i in num_list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
    total += i
print("{} {} {}".format(smallest, largest, total))