x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
if (x == 2 or y == 2) or (x in a and y not in a) or (x in b and y not in b):
    print('No')
else:
    print('Yes')