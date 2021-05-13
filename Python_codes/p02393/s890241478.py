x = raw_input()
x_list = x.split(" ")

x_list = map(int, x_list)

max = min = mid = 0
for i in range(1,3):
    if x_list[max] < x_list[i]:
        mid = max
        max = i
    elif x_list[min] > x_list[i]:
        mid = min
        min = i
    else:
        mid = i

print("%d %d %d" %(x_list[min], x_list[mid], x_list[max]))