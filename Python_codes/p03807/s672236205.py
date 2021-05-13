x=int(input())
y=list(map(int, input().split()))
if x==1:
	print('YES')
else:
	if sum(y)%2==1:
		print('NO')
	else:
		print('YES')