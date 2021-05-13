def actual(x, y):
    group1 = {1, 3, 5, 7, 8, 10, 12}
    group2 = {4, 6, 9, 11}
    group3 = {2}

    for group in [group1, group2, group3]:
        if x in group and y in group:
            return 'Yes'

    return 'No'

x, y = map(int, input().split())
print(actual(x, y))