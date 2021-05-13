import sys
dic = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]  
for s in sys.stdin.read().lower():
	if s == '':
		break
	for i in s:
		for j in range(0, 26):
			if dic[j][0] == i.lower():
				dic[j][1] += 1
				break
for i in range(0, 26):
	print dic[i][0], ':', dic[i][1]