import sys

input_list = input().split(" ")
input_list = list(map(int, input_list))

w = input_list[0]
h = input_list[1]
x = input_list[2]
y = input_list[3]
r = input_list[4]

if 0 <= x - r and x + r <= w:
    if 0 <= y - r and y + r <= h:
        print("Yes")
        sys.exit()

print("No")