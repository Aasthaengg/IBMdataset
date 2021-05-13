import sys
from collections import deque 

def input():
	return sys.stdin.readline().rstrip()

input()
a = deque()

while True:
	op = input().split()
	if not op:
		break
	if op[0] == 'insert':
		a.appendleft(int(op[1]))
	elif op[0] == 'delete':
		try:
			a.remove(int(op[1]))
		except:
			pass
	elif op[0] == 'deleteFirst':
		a.popleft()
	elif op[0] == 'deleteLast':
		a.pop()

while True:
	x = a.popleft()
	print(x, end="")
	if len(a)>0:
		print(" ", end="")
	else:
		print("")
		break

