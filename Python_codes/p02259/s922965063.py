
def bubble_sort(buff):
	count = 0
	k = len(buff) - 1
	for i in xrange(k):
		for j in xrange(k, i, -1):
			if buff[j - 1] > buff[j]:
				count += 1
				temp = buff[j]
				buff[j] = buff[j - 1]
				buff[j - 1] = temp
	print " ".join(map(str, buff))
	print count

N = int(raw_input())
buff = map(int, raw_input().split(' '))
bubble_sort(buff)