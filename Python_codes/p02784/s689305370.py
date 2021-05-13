h, n = map(int, input().split())
if h <= sum(list(map(int, input().split()))):
    print('Yes')
else:
    print('No')
