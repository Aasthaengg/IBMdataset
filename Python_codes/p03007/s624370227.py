import bisect

def main():
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	idx = bisect.bisect_left(a,0)
	if idx == 0:
		idx = 1
	elif idx == n:
		idx = -1
	cur_min = a[0]
	cur_max = a[-1]
	res = []
	for n in a[1:idx]:
		res.append('{} {}'.format(cur_max,n))
		cur_max -= n
	for n in a[idx:-1]:
		res.append('{} {}'.format(cur_min,n))
		cur_min -= n
	res.append('{} {}'.format(cur_max,cur_min))
	print(cur_max-cur_min)
	for r in res:
		print(r)

if __name__ == '__main__':
	main()