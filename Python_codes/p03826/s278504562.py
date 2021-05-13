len = input().split()
len_i = [int(s) for s in len]

area1 = len_i[0] * len_i[1]
area2 = len_i[2] * len_i[3]

print(max(area1, area2))