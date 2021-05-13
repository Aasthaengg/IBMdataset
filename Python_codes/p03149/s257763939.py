import sys
if sys.platform =='ios':
	sys.stdin=open('input.txt')

l = list(map(int,input().split()))

l.sort()

#print(''.join(list(map(str, l))))

if ''.join(list(map(str, l)))=='1479':
	print('YES')
else:
	print('NO')