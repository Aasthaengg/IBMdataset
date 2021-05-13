#!/usr/bin/env python
#-*- coding:utf-8 -*-
from collections import deque

def process_task(task,qua, elapsed_time, complete_task):
	exe_task = task.popleft()
	t = int(exe_task[1])
	q = int(qua)

	if t-q  > 0:
		exe_task[1] = (t - q)
		task.append(exe_task)
		elapsed_time += q
	else:	
		elapsed_time += t
		complete_task.append([exe_task[0], elapsed_time])

	return elapsed_time,complete_task

def main():
	n,q = map(int, raw_input().split())
	task = [raw_input().split() for _ in range(n)]
	que = deque(task)
	ela_time = 0
	comp_task = []

	while len(que) != 0:
		ela_time , comp_task= process_task(que, q, ela_time,comp_task)	

	for i in comp_task:
		print i[0], i[1]

#def test():

if __name__ == '__main__':
	main()
	#test()