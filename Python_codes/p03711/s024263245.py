x, y = map(int, input().split())

group = ['a', 'c', 'a', 'b', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'a']

if group[x-1] == group[y-1]:
    print('Yes')
else:
    print('No')
