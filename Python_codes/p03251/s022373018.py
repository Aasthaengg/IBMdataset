n, m, x, y = map(int, input().split())
xm = list(map(int, input().split()))
ym = list(map(int, input().split()))
print('No War' if max([x] + xm) < min([y] + ym) else 'War')
