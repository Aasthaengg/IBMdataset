x, y = [int(s) for s in input().split()]
temp_list = [{1, 3, 5, 7, 8, 10, 12}, {4, 6, 9, 1}, {2}]
ans = "No"
for temp in temp_list:
    if x in temp and y in temp:
        ans = "Yes"
print(ans)