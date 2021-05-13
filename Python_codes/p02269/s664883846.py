import time

n = int(input())
#t1 = time.time()

S = set()
for i in range(0,n):
	lst = list(input().split())
	if lst[0] == 'insert':
		S.add(lst[1])
	elif lst[0] == 'find':
		if lst[1] in S:
			print('yes')
		else:
			print('no')

#S = []
#for i in range(0,n):
#	lst = list(input().split())
#	if lst[0] == 'insert':
#		S.append(lst[1])
#	elif lst[0] == 'find':
#		if S.count(lst[1]) != 0:
#			print('yes')
#		else:
#			print('no')

#t2 = time.time()
#elapsed = t2-t1
#print('経過時間:{0}'.format(elapsed))
