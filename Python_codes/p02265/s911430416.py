import sys
from collections import deque

def doubly_lined_list():
	n = int(input())
	Q = deque()

	for i in range(n):
		line = sys.stdin.readline()
		command = line.split()[0]

		if command == 'insert':
			Q.appendleft(line.split()[1])
		elif command == 'delete':
			try:
				Q.remove(line.split()[1])
			except:
				pass
		elif command == 'deleteFirst':
			Q.popleft()
		elif command == 'deleteLast':
			Q.pop()

	print(' '.join(Q))

if __name__ == '__main__':
	doubly_lined_list()