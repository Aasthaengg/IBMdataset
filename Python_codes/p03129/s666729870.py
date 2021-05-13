import sys


line = sys.stdin.readline()
N, K = line.split(" ")
N = int(N)
K = int(K)
if N%2 == 0:
	if K <= (N/2):
		print("YES")
	else:
		print("NO")	
else:
	if K <= (N/2 + 1):
		print("YES")
	else:
		print("NO")