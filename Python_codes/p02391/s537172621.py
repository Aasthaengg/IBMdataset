(a, b) = map(lambda s:int(s), input().split())

if a < b:
	cmp = '<'
elif a > b:
	cmp = '>'
else:
	cmp = '=='

print('a', cmp, 'b')