import sys
n = input()
a_n = map(int,raw_input().split())
j = -1
for i in range(n):
	if j == -1 :
			sys.stdout.write(str(a_n[j]))
			j -= 1
	else :		
		print (' '),
		sys.stdout.write(str(a_n[j]))
		j -= 1
print ''