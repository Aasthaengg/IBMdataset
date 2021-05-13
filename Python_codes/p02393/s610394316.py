arr = [int(x) for x in input().split(' ')]
arr_sorted = sorted(arr)
str_sorted = ' '.join(str(x) for x in arr_sorted)
print(str_sorted)