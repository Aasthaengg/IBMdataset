S = str(input())
T = str(input())

s = len(S)
t = len(T)

import re

if t > s:
	print("UNRESTORABLE")
	exit()

pos = -1
wani = 0

for i in range (0, s-t+1):
	wani = 0
	for j in range (0,t):
		if	S[i+j] != T[j] and S[i+j] !='?':
			wani = 1
	if wani == 0:
		pos = i        
        
if pos == -1:
	print("UNRESTORABLE")
	exit()

A = []
for i in range (0, s):
	A.append(S[i])

for i in range (0, t):
	A[pos+i] = T[i]

for i in range (0, s):
	if A[i] == '?':
		A[i] = 'a'

print(*A, sep='')