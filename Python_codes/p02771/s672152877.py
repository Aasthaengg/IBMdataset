ls = list(input().split(' '))
if ls.count(ls[0]) == 2 or ls.count(ls[1]) == 2:
    print('Yes')
else:
    print('No')