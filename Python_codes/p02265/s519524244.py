from collections import deque

que = deque([])
n = int(input())
for i in range(0, 	n):
	a = input()
	if a == 'deleteFirst':
		que.popleft()
#		print(a)
#		print(que)
	elif a == 'deleteLast':
		que.pop()
#		print(a)
#		print(que)
	else:
		a, b = a.split()
		b = int(b)
		if a == 'insert':
			que.appendleft(b)
#			print('{0} {1}'.format(a,b))
#			print(que)
		elif a == 'delete':
			if que.count(b) != 0:
				que.remove(b)
#			print('{0} {1}'.format(a, b))

print(*que)

#while not len(que) == 0:
#	if len(que) == 1:
#		print(que.pop())
#	else:
#		print(que.pop(), end=' ')

