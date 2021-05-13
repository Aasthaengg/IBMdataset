x, y = [int(s) for s in input().split()]
temp_list = [-1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
print("Yes" if temp_list[x] == temp_list[y] else "No")