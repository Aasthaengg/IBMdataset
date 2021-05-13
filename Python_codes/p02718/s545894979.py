n, m = map(int, input().split())
lis = sorted(list(map(int, input().split())), reverse=True)
limit = sum(lis) / (4 * m)
if lis[m -1 ] >= limit:
    print('Yes')
else:
    print('No')
