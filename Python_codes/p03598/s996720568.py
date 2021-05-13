n = int(input())
k = int(input())
x_list = [int(s) for s in input().split()]
print(sum([min(x, abs(k - x)) * 2 for x in x_list]))