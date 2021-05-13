import numpy as np
import sys
readline = sys.stdin.readline
read = sys.stdin.read

b = readline().rstrip()
if b == 'A':
	print('T')
elif b == 'T':
	print('A')
elif b == 'G':
	print('C')
else:
	print('G') 
