#!/usr/bin/env python
#-*- coding:utf-8 -*-
from collections import deque

def parse_cmd(deque,input_cmd):
	if input_cmd[0] == 'insert':
		deque.appendleft(input_cmd[1])
	elif input_cmd[0] == 'delete':
		try:
			deque.remove(input_cmd[1])
		except:
			pass
	elif input_cmd[0] == 'deleteFirst':
		deque.popleft()
	elif input_cmd[0] == 'deleteLast':
		deque.pop()
		
def main():
	que = deque()
	n = int(raw_input())
	cmd = [raw_input().split() for _ in range(n)]
	
	for i in cmd:
		parse_cmd(que,i)
	
	print " ".join(que)


#def test():

if __name__ == '__main__':
	main()
	#test()