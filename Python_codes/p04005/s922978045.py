A, B, C = map(int, input().split())
if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
else:
    array = [A, B, C]
    sort_array = sorted(array, reverse=True)
    print(sort_array[1] * sort_array[2])
