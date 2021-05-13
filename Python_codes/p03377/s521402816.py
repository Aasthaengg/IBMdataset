line = input()
known_cat_num, unknow_num, expected_cat_num = [int(n) for n in line.split()]
if (expected_cat_num < known_cat_num
        or expected_cat_num - known_cat_num > unknow_num):
    print("NO")
else:
    print("YES")