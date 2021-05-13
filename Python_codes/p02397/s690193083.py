import sys


list_line = sys.stdin.readlines()

for index, element in enumerate(list_line):
    list_line[index] = element.rstrip('\n')

for element in list_line:
    x_y_list = element.split(" ")
    x = int(x_y_list[0])
    y = int(x_y_list[1])
    if x == 0 and y == 0:
        sys.exit()
    if x > y:
        print(str(y) + " " + str(x))
    else:
        print(element)