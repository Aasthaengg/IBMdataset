n = int(input())
a_list = [int(x) for x in input().split()]
print(sum([a - 1 for a in a_list]))