n = int(input())
aa = [int(i) for i in input().split()]
flg = True
for a in aa:
	if a % 2 == 0:
		if a % 3 != 0 and a % 5 != 0:
			flg = False
print('APPROVED' if flg else 'DENIED')