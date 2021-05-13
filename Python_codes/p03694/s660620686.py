n = int(input())
a_list = sorted([int(x) for x in input().split()])
print(a_list[-1] - a_list[0])