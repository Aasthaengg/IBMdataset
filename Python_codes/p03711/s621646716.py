x, y = map(int, input().split())
g = [set([1, 3, 5, 7, 8, 10, 12]), set([4, 6, 9, 11]), set([2])]
for s in g:
    if x in s and y in s:
        print('Yes')
        break
else:
    print('No')
