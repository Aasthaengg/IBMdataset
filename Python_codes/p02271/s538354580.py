import sys
#fin = open("test.txt", "r")
fin = sys.stdin

n = int(fin.readline())
A = list(map(int, fin.readline().split()))
q = int(fin.readline())
m_list = list(map(int, fin.readline().split()))

for m in m_list:
	can_compose = False
	s = [[] for i in range(n)] #s[i][m]??§???A[i]?????§???????´???§m????????????????????????????????????
	for i in range(n):
		s[i] = [False for i in range(m + 1)]

	for j in range(m + 1):
		if j == A[0]:
			s[0][j] = True
		else:
			s[0][j] = False
		
	if s[0][m]:
		can_compose = True
		
	if not can_compose:
		for i in range(1, n):
			for j in range(m + 1):
				if j == A[i]:
					s[i][j] = True
				elif s[i - 1][j]:
					s[i][j] = True
				else:
					if j - A[i] >= 0:
						s[i][j] = s[i - 1][j - A[i]]
			
			if s[i][m]:
				can_compose = True
				break

	if can_compose:
		print("yes")
	else:
		print("no")