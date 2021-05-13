a,b = map(str, input().split())
sq = int(a+b)**0.5
print('Yes' if sq.is_integer() else 'No')