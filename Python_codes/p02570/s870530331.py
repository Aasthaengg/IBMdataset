import sys

num_list = [int(i) for i in input().split()]

if num_list[0] / num_list[2] <= num_list[1]:
    print("Yes")
else:
    print("No")
