x, y = map(int, input().split())
group = 'acababaababa'
print('Yes' if group[x-1] == group[y-1] else 'No')
