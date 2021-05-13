
x, y = map(int, input().split())

grp_dict = {
    1: 'A',
    2: 'C',
    3: 'A',
    4: 'B',
    5: 'A',
    6: 'B',
    7: 'A',
    8: 'A',
    9: 'B',
    10: 'A',
    11: 'B',
    12: 'A',
}

print('Yes' if grp_dict[x] == grp_dict[y] else 'No')
