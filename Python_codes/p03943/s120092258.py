a,b,c = map(int, input().split())
if 2*max([a,b,c]) == sum([a,b,c]):
    print('Yes')
else:
    print('No')