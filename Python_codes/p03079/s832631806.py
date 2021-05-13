A, B, C = map(int, input().split())
l = [A, B, C]
print('Yes' if len(set(l)) == 1 else 'No')
