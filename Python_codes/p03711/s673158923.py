l = [4, 6, 9, 11]
x, y = map(int, input().split())
if x == 2 or y == 2:
    print('No')
elif x in l and y in l:
    print('Yes')
elif x not in l and y not in l:
    print('Yes')
else:
    print('No')