# B - Problem Set
def is_create(dic_d, t):
	for ti in t:
		if not ti in dic_d.keys():
			return False
		elif dic[ti] == 0:
			return False
		else:
			dic[ti] -= 1	
	
	return True


n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

dic = dict()

for di in d:
	dic.setdefault(di, 0)
	dic[di] += 1
	'''if di in dic.keys():
		dic[di] += 1
	else:
		dic[di] = 1'''

if is_create(dic, t):
	print('YES')
else:
	print('NO')