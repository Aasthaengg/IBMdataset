S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
rst = 'None'
for i in alp:
	if not i in S:
		rst = i
		break
print(rst)
