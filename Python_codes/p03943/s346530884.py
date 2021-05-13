l = map(int, input().split())
l = sorted(l, reverse=True)
if l[0] == sum(l[1:]):
    print('Yes')
else:
    print('No')
