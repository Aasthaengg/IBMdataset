n, *lst = map(int, open(0).read().split())
print('NO' if sum(lst) % 2 else 'YES')