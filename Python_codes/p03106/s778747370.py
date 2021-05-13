from collections import deque

if __name__ == '__main__':

	a,b,k = map(int,input().split())

	mini = min(a,b)
	d = deque()
	for x in range(1,mini+1):
		a2 = a % x
		b2 = b % x
		if a2 == 0 and b2 == 0:
			d.appendleft(x)
	print(d[k-1])


