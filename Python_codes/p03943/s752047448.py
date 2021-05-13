a, b, c = map(int, input().split())

l = [a, b, c]
l = sorted(l, reverse=True)

if l[0] == l[1]+l[2]:
    print('Yes')
else:
    print('No')
