i = [int(each) for each in input().split()]
print(min(i[1], i[2]), max(i[1] + i[2] - i[0], 0))