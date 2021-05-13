x, y = map(int, input().split())
group = [[1,3,5,7,8,10,12], [4,6,9,11]]

if x == 2 or y == 2:
    print('No')
elif x in group[0]:
    if y in group[0]:
        print('Yes')
    else:
        print('No')
elif x in group[1]:
    if y in group[1]:
        print('Yes')
    else:
        print('No')