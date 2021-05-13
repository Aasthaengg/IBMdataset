#16D8101014F 久留米 竜之介 Kurume Ryunosuke 2018/5/9 python3
import collections 
List=collections.deque()
n=int(input())
for i in range(n):
	command=input().split()
	if command[0] == 'insert':
		List.appendleft(command[1])		
	elif command[0] == 'delete':
		try:
			List.remove(command[1])
		except:
			pass
	elif command[0] == 'deleteFirst':
		List.popleft()	
	elif command[0] == 'deleteLast':
		List.pop()
		
print(*List)

